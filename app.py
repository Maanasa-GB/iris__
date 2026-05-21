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
