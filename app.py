import os
import cv2
import numpy as np
import face_recognition
import concurrent.futures
from flask import Flask, render_template, jsonify
import pickle
import requests
from io import BytesIO
from PIL import Image
from datetime import datetime
import logging

app = Flask(__name__)

# Setup logging
if not os.path.exists('logs'):
    os.makedirs('logs')
logging.basicConfig(filename='logs/app.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

# ESP32-CAM IP
ESP32_CAM_IP = "http://192.168.137.208/cam-hi.jpg"

# Load known face encodings and names (cache them for stability and performance)
try:
    with open("models/face_encodings.pkl", "rb") as f:
        data = pickle.load(f)
    known_face_encodings = data["encodings"]
    known_face_names = data["names"]
    logging.info("Successfully loaded known face encodings and names.")
except Exception as e:
    logging.error(f"Error loading face encodings: {e}")
    known_face_encodings, known_face_names = [], []

# Attendance history list
attendance_history = []

def get_frame_from_esp32():
    """Fetch a frame from the ESP32-CAM."""
    try:
        response = requests.get(ESP32_CAM_IP, timeout=5)
        img_array = np.array(Image.open(BytesIO(response.content)))
        img_array = cv2.resize(img_array, (640, 480))  # Resize to optimize performance
        return img_array
    except Exception as e:
        logging.error(f"Error getting frame from ESP32-CAM: {e}")
        return None

def process_frame_in_parallel(frame):
    """Process a frame to detect and encode faces."""
    try:
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
        return face_encodings, face_locations
    except Exception as e:
        logging.error(f"Error processing frame: {e}")
        return [], []

def recognize_faces(face_encodings, frame, face_locations):
    """Recognize faces and draw bounding boxes."""
    recognized_names = []
    unknown_faces = []
    try:
        for (top, right, bottom, left), encoding in zip(face_locations, face_encodings):
            matches = face_recognition.compare_faces(known_face_encodings, encoding)
            name = "Unknown"
            face_distances = face_recognition.face_distance(known_face_encodings, encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]
                recognized_names.append(name)
            else:
                recognized_names.append("Unknown")
                # Crop and save the unknown person's image
                unknown_face = frame[top:bottom, left:right]
                unknown_faces.append(unknown_face)
            
            # Draw rectangle around face and add name
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.putText(frame, name, (left + 6, bottom + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    except Exception as e:
        logging.error(f"Error recognizing faces: {e}")
    
    return recognized_names, frame, unknown_faces

@app.route('/')
def index():
    return render_template('index.html', attendance_history=attendance_history)

@app.route('/stream')
def stream():
    """Stream frame data and return the face recognition results."""
    frame = get_frame_from_esp32()
    if frame is None:
        return jsonify({"status": "light_off", "recognized_faces": [], "unknown_faces": [], "original_image": "", "processed_image": ""})

    # Process frame in parallel
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(process_frame_in_parallel, frame)
        face_encodings, face_locations = future.result()

    recognized_names, processed_frame, unknown_faces = recognize_faces(face_encodings, frame, face_locations)

    # Update attendance history
    for name in recognized_names:
        attendance_history.append((len(attendance_history) + 1, name, datetime.now().strftime("%Y-%m-%d"), datetime.now().strftime("%H:%M:%S")))

    # Save original and processed images
    original_image_path = "static/original_image.jpg"
    processed_image_path = "static/processed_image.jpg"
    try:
        cv2.imwrite(original_image_path, frame)
        cv2.imwrite(processed_image_path, processed_frame)
    except Exception as e:
        logging.error(f"Error saving images: {e}")

    # Save unknown faces' images
    unknown_faces_paths = []
    for i, unknown_face in enumerate(unknown_faces):
        unknown_face_path = f"static/unknown_face_{i + 1}.jpg"
        try:
            cv2.imwrite(unknown_face_path, unknown_face)
            unknown_faces_paths.append(unknown_face_path)
        except Exception as e:
            logging.error(f"Error saving unknown face image: {e}")

    status = "light_on" if len(recognized_names) > 0 else "light_off"

    return jsonify({
        "status": status,
        "recognized_faces": recognized_names,
        "unknown_faces": unknown_faces_paths,
        "original_image": original_image_path,
        "processed_image": processed_image_path
    })

if __name__ == '__main__':
    app.run(debug=True)
