import face_recognition
import pickle
known_face_encodings = []
known_face_names = []
image = face_recognition.load_image_file("S:\z5919413266825_1010f9022e391122252d26a397255330.jpg")
encoding = face_recognition.face_encodings(image)[0]
known_face_encodings.append(encoding)
known_face_names.append("Thanh An")
data = {"encodings": known_face_encodings, "names": known_face_names}
with open("models/face_encodings.pkl", "wb") as f:
    pickle.dump(data, f)
