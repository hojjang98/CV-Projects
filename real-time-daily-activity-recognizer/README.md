# 🎥 Real-Time Daily Activity Recognizer

> *"Your webcam knows what you’re doing — let’s teach it how."*

This project explores real-time human activity classification using webcam video and a CNN-based model trained on crawled images.  
Inspired by modern computer vision applications, it aims to simulate how AI can recognize common daily behaviors like brushing teeth or eating.

---

## 🎯 Project Goal

- Build a real-time daily activity recognition system using computer vision
- Crawl and prepare a custom dataset of human actions
- Train a CNN-based model with transfer learning (e.g., MobileNetV2)
- Use OpenCV to connect webcam input with live predictions

---

## 📁 Dataset

- **Source**: Images crawled using Google Images (via Selenium)  
- **Categories**:  
  `brushing_teeth`, `drinking`, `eating`, `typing`,  
  `sleeping`, `reading`, `washing_face`, `walking`

- **Images per class**: Around 350+ planned  
- **Availability**:  
  The dataset is **excluded from this repository** to avoid copyright issues.

> ⚠️ All images used in this project were collected solely for educational purposes and are stored locally.  
> To build your own dataset, use the `activity-crawling.ipynb` notebook 

---

## 🔧 Techniques Used

- Convolutional Neural Networks (CNN)
- Transfer Learning (MobileNetV2)
- Image Augmentation (`ImageDataGenerator`)
- Real-time prediction with OpenCV
- Evaluation: Confusion Matrix, Visual Prediction Output

---

## 🧱 Project Structure

```bash
real-time-daily-activity-recognizer/
├── .gitignore
├── experiment_logs/           # Experiment markdown logs
├── figures/                   # Training curves, confusion matrix, result plots
├── images/                    # Crawled raw image data (organized by class)
├── notebook/                  # Jupyter notebooks for model training/inference
├── requirements.txt
└── README.md

