import face_recognition as fr
import cv2
import numpy as np
import json

def mark_faces(frame, face_locations, face_names):
    # Mark the detected faces with rectangles and display names
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(frame, name, (left + 6, bottom + 6), cv2.FONT_HERSHEY_DUPLEX, 1.0, (255, 255, 255), 1)
    return frame

def find_faces(frame):
    face_names = []
    face_locations = []

    # Convert the frame to RGB format for face recognition
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Find face locations and encodings in the frame
    face_locations = fr.face_locations(rgb_frame)
    face_encodings = fr.face_encodings(rgb_frame, face_locations)

    for face_encoding in face_encodings:
        # Compare the face encodings with known face encodings
        matches = fr.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"

        face_distances = fr.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            # If a match is found, assign the corresponding known face name
            name = known_face_names[best_match_index]

        face_names.append(name)

    # Mark the faces in the frame with rectangles and names
    frame = mark_faces(frame, face_locations, face_names)
    return frame

def load_known_faces(filename):
    # Load known faces from a JSON file
    with open(filename, 'r') as file:
        data = json.load(file)
    known_images = []
    known_face_encodings = []
    known_face_names = []
    for entry in data:
        path = entry['path']
        name = entry['name']
        try:
            # Load image and obtain the face encoding
            image = fr.load_image_file(path)
            encoding = fr.face_encodings(image)[0]
            known_images.append(image)
            known_face_encodings.append(encoding)
            known_face_names.append(name)
        except:
            print(f"Invalid path for '{name}' face!")

    return known_images, known_face_encodings, known_face_names

# Load known faces from the JSON file
known_images, known_face_encodings, known_face_names = load_known_faces("known_faces.json")

# Specify the path to the image file you want to process
path = "elon&sundar.jpg"

# Read the image file
img = cv2.imread(path)

# Find and recognize faces in the image
recognised_faces = find_faces(img)

# Display the image with recognized faces
cv2.imshow("Image file", recognised_faces)
cv2.waitKey(0)
cv2.destroyAllWindows()
