import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# Load model
MODEL_PATH = "garbage_classifier.h5"
model = tf.keras.models.load_model(MODEL_PATH)

# Labels (must match training order)
class_names = ['cardboard', 'glass', 'metal', 'paper', 'plastic', 'trash']

st.title("📷 Garbage Classification")
st.write("Capture a photo and classify it into one of 6 categories.")

# Webcam input
img_file = st.camera_input("Take a picture")

if img_file:
    img = Image.open(img_file).convert("RGB")
    st.image(img, caption="Captured Image", use_container_width=True)

    # Preprocess
    img = img.resize((224, 224))
    x = np.expand_dims(np.array(img).astype("float32") / 255.0, axis=0)

    # Predict
    probs = model.predict(x, verbose=0)[0]
    pred_idx = np.argmax(probs)
    pred_class = class_names[pred_idx]
    confidence = probs[pred_idx]

    # Results
    st.subheader("Prediction Result")
    st.write(f"**Class:** {pred_class}")
    st.write(f"**Confidence:** {confidence:.2%}")

    # Show all class probabilities
    st.bar_chart(dict(zip(class_names, probs)))
