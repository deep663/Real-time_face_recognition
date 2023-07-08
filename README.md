# Face Recognition

This project demonstrates face recognition using the `face_recognition` library in Python. It includes two code snippets: one for face recognition with an image and another for real-time face recognition with a webcam. Both snippets utilize the `face_recognition` library to detect faces, match them with known faces, and mark them with rectangles and names.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/deep663/Real-time_face_recognition.git
   ```

2. Install the required libraries:

   ```bash
   pip install face_recognition opencv-python numpy
   ```

3. Prepare the known faces:

   - Create a JSON file named `known_faces.json` in the project directory.
   - Define the known faces by providing the image path and name in the following format:

     ```json
     [
       {
         "path": "path/to/known_face_1.jpg",
         "name": "Known Face 1"
       },
       {
         "path": "path/to/known_face_2.jpg",
         "name": "Known Face 2"
       },
       ...
     ]
     ```

## Usage

### Face Recognition with Image

1. Specify the image file path in the code:

   ```python
   path = "path/to/image_file.jpg"
   ```

2. Run the script:

   ```bash
   python face_recognition_with_image.py
   ```

3. The script will display the image with recognized faces, marking them with rectangles and displaying the names.

### Face Recognition with Webcam

1. Run the script:

   ```bash
   python face_recognition_with_webcam.py
   ```

2. The script will open a window displaying the webcam feed with recognized faces, marking them with rectangles and displaying the names.

3. Press 'q' to exit the program.

## Snapshots

### Face Recognition with Image
![Face Recognition with Image](https://github.com/deep663/Real-time_face_recognition/assets/62834469/1af6f2f7-b7fb-4599-a5e9-09f5e9a9c0fc)

### Face Recognition with Webcam
![Face Recognition with Webcam](https://github.com/deep663/Real-time_face_recognition/assets/62834469/6ba7137e-420f-43e8-a981-407a7c02f698)

## Contributing

Contributions are welcome! If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
```

Make sure to replace `snapshot_image.png` and `snapshot_webcam.png` with actual snapshots of your project results.
