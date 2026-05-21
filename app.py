import streamlit as st
import cv2
import numpy as np
import hashlib
from PIL import Image

# -----------------------------
# PAGE CONFIG
# -----------------------------

st.set_page_config(
    page_title="Iris Password Generator",
    page_icon="👁️",
    layout="centered"
)

# -----------------------------
# CUSTOM CSS
# -----------------------------

st.markdown(
    """
    <style>
    .main {
        background-color: #0f172a;
        color: white;
    }

    .title {
        font-size: 42px;
        font-weight: bold;
        text-align: center;
        color: #38bdf8;
        margin-bottom: 10px;
    }

    .subtitle {
        text-align: center;
        color: #cbd5e1;
        margin-bottom: 40px;
    }

    .password-box {
        background-color: #1e293b;
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #38bdf8;
        text-align: center;
        font-size: 24px;
        font-weight: bold;
        color: #22c55e;
    }

    .footer {
        text-align: center;
        margin-top: 40px;
        color: gray;
        font-size: 14px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# -----------------------------
# TITLE
# -----------------------------

st.markdown('<div class="title">👁️ Iris Password Generator</div>', unsafe_allow_html=True)

st.markdown(
    '<div class="subtitle">Generate a secure password from your iris image</div>',
    unsafe_allow_html=True
)

# -----------------------------
# PASSWORD GENERATOR
# -----------------------------

def generate_password(image):

    # Convert PIL image to OpenCV format
    image = np.array(image)

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    # Resize for consistency
    gray = cv2.resize(gray, (250, 250))

    # Blur slightly
    gray = cv2.GaussianBlur(gray, (5, 5), 0)

    # Edge enhancement
    edges = cv2.Canny(gray, 100, 200)

    # Convert image to bytes
    image_bytes = edges.tobytes()

    # SHA256 hash
    hash_value = hashlib.sha256(image_bytes).hexdigest()

    # Password characters
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()"

    # Generate password
    password = ""

    for i in range(24):
        idx = int(hash_value[i:i+2], 16) % len(chars)
        password += chars[idx]

    return password

# -----------------------------
# FILE UPLOAD
# -----------------------------

uploaded_file = st.file_uploader(
    "Upload Iris Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.image(image, caption="Uploaded Iris", use_container_width=True)

    if st.button("Generate Password"):

        with st.spinner("Analyzing iris pattern..."):

            password = generate_password(image)

        st.success("Password Generated Successfully")

        st.markdown(
            f'<div class="password-box">{password}</div>',
            unsafe_allow_html=True
        )

        st.download_button(
            label="Download Password",
            data=password,
            file_name="iris_password.txt",
            mime="text/plain"
        )

# -----------------------------
# INFO SECTION
# -----------------------------

with st.expander("How It Works"):

    st.write(
        """
        1. Upload an iris image.
        2. The app processes the iris texture.
        3. Edge patterns are extracted.
        4. A SHA-256 hash is generated.
        5. The hash becomes a secure password.
        """
    )

# -----------------------------
# FOOTER
# -----------------------------

st.markdown(
    '<div class="footer">Built with Streamlit + OpenCV</div>',
    unsafe_allow_html=True
)
