import face_recognition as fr
import cv2
import numpy as np
import json


def load_known_faces(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    known_images = []
    known_face_encodings = []
    known_face_names = []
    for entry in data:
        path = entry['path']
        name = entry['name']
        try:
            image = fr.load_image_file(path)
            encoding = fr.face_encodings(image)[0]
            known_images.append(image)
            known_face_encodings.append(encoding)
            known_face_names.append(name)
        except:
            print(f"Invalid path for '{name}' face!")

    return known_images, known_face_encodings, known_face_names


known_images, known_face_encodings, known_face_names = load_known_faces("known_faces.json")


def mark_faces(frame, face_locations, face_names):
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(frame, name, (left + 6, bottom + 6), cv2.FONT_HERSHEY_DUPLEX, 1.0, (255, 255, 255), 1)
    return frame


def find_faces(frame):
    face_names = []
    face_locations = []

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    face_locations = fr.face_locations(rgb_frame)
    face_encodings = fr.face_encodings(rgb_frame, face_locations)

    for face_encoding in face_encodings:
        matches = fr.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"

        face_distances = fr.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = known_face_names[best_match_index]

        face_names.append(name)

    frame = mark_faces(frame, face_locations, face_names)
    return frame


video_capture = cv2.VideoCapture(0)

while True:
    ret, frame = video_capture.read()

    frame = find_faces(frame)

    cv2.imshow("Live-webcam", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
