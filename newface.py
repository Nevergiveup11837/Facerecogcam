import face_recognition
import pickle
import os
import cv2
import numpy as np

def enhance_image(image):
    yuv = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)
    yuv[:, :, 0] = cv2.equalizeHist(yuv[:, :, 0])
    enhanced_image = cv2.cvtColor(yuv, cv2.COLOR_YUV2BGR)
    return enhanced_image

def main():
    known_face_encodings = []
    known_face_names = []

    image_path = input("Enter the path to the image: ")

    if not os.path.exists(image_path):
        print(f"Error: File not found at {image_path}")
        print("Fix: Please check the path and ensure the image file exists.")
        return

    person_name = input("Enter the name of the person: ").strip()

    if not person_name:
        print("Error: Name cannot be empty.")
        print("Fix: Please enter a valid name for the person being registered.")
        return

    try:
        image = face_recognition.load_image_file(image_path)
        image_cv2 = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        enhanced_image = enhance_image(image_cv2)

        face_encodings = face_recognition.face_encodings(enhanced_image)

        if len(face_encodings) == 0:
            raise ValueError("No face detected in the image.")

        encoding = face_encodings[0]
        known_face_encodings.append(encoding)
        known_face_names.append(person_name)

        if os.path.exists("models/face_encodings.pkl"):
            with open("models/face_encodings.pkl", "rb") as f:
                data = pickle.load(f)
            known_face_encodings = data["encodings"] + known_face_encodings
            known_face_names = data["names"] + known_face_names
        
        data = {"encodings": known_face_encodings, "names": known_face_names}
        with open("models/face_encodings.pkl", "wb") as f:
            pickle.dump(data, f)

        print(f"Successfully encoded and saved face for {person_name}!")
    
    except FileNotFoundError:
        print(f"Error: File not found at {image_path}")
        print("Fix: Please check the path and make sure the image exists.")

    except ValueError as ve:
        print(f"Error: {ve}")
        print("Fix: Ensure the image contains at least one clear face for detection.")

    except Exception as e:
        print(f"Unknown error: {e}")
        print("Fix: Check the image and try again, or contact support if the issue persists.")

if __name__ == "__main__":
    main()
