import streamlit as st
import pandas as pd
from PIL import Image

# Set page title
st.set_page_config(page_title="Face Recognition Attendance", layout="wide")

# Title
st.title("📸 Face Recognition Attendance System")

# Upload image section
st.header("Upload Class Image for Attendance")
uploaded_file = st.file_uploader("Upload an image...", type=["png", "jpg", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Simulated student data (mocked for now)
    detected_students = [
        {"Name": "Amit Sharma", "Enrollment No": "2023ME101", "Year": "2nd"},
        {"Name": "Priya Gupta", "Enrollment No": "2023CS205", "Year": "1st"},
        {"Name": "Rohan Verma", "Enrollment No": "2022EE303", "Year": "3rd"},
        {"Name": "Yash Drall", "Enrollment No": "22117016", "Year": "3rd"},
      {"Name": "Priyanshu Gupta", "Enrollment No": "20116018", "Year": "3nd"},
      {"Name": "Priyam Pandey", "Enrollment No": "23115082", "Year": "2nd"},
    ]
    
    # Convert to DataFrame
    df = pd.DataFrame(detected_students)

    # Show detected students
    st.subheader("🎓 Detected Students")
    st.dataframe(df, hide_index=True)

    # Show total students detected
    total_students = len(detected_students)
    st.subheader(f"📊 Total Students Detected: {total_students}")

# Footer
st.markdown("---")
st.markdown("🔒 **Secure & Automated Attendance System** | Designed for classrooms, libraries, and security gates.")

