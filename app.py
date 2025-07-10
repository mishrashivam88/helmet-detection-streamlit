import streamlit as st
import torch
import cv2
import numpy as np
from PIL import Image
import tempfile

st.set_page_config(page_title="Helmet Detection", layout="wide")
st.title("🪖 Helmet Detection App")
st.write("Upload an image and detect helmets using YOLOv8 (via torch.hub).")

# Load YOLOv8 model
@st.cache_resource
def load_model():
    return torch.hub.load("ultralytics/yolov5", "custom", path="yolov8n.pt", force_reload=False)

model = load_model()

# Upload image
uploaded_file = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    img_array = np.array(image)

    st.image(image, caption="Uploaded Image", use_column_width=True)

    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp:
        temp_filename = tmp.name
        cv2.imwrite(temp_filename, cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR))

    with st.spinner("🔍 Detecting helmets..."):
        results = model(temp_filename)
        results.render()

    st.image(results.ims[0], caption="Detection Result", use_column_width=True)
