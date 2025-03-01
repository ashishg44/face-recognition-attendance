import streamlit as st
import cv2
import numpy as np
from PIL import Image

st.title("Face Recognition Attendance System 📸")

# Upload image
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Convert the uploaded file to an OpenCV image
    image = Image.open(uploaded_file)
    img_array = np.array(image)

    # Display the uploaded image
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Load a pre-trained face detection model (Haar Cascade)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

    # Convert image to grayscale
    gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Show detected faces
    if len(faces) > 0:
        st.success(f"✅ Detected {len(faces)} face(s)!")
    else:
        st.warning("⚠ No faces detected. Try another image.")

