# 🎥 Real-Time Daily Activity Recognizer

> *"Your webcam knows what you're doing — let's teach it how."*  

This project builds a real-time human activity recognition system powered by computer vision and deep learning.  
The system uses a webcam and a transfer-learned CNN model to classify everyday activities such as brushing teeth, reading, or walking.

---

## 🎯 Objectives

- Build a live activity recognizer using webcam input and a CNN-based classifier  
- Collect a custom dataset of daily activities using Selenium-based image crawling  
- Train an image classifier using transfer learning (EfficientNetB0, MobileNetV2, etc.)  
- Use OpenCV to perform real-time inference with webcam video feed  

---

## 📁 Dataset

- **Source**: Google Images (via Selenium automation)  
- **Classes**:  
  - `brushing_teeth`  
  - `drinking`  
  - `eating`  
  - `typing`  
  - `sleeping`  
  - `reading`  
  - `washing_face`  
  - `walking`  

- **Images per class**: Approx. 350~3000 images each (customizable)  
- **Availability**:  
  The dataset is **excluded** from the repository to avoid copyright violations.  

> ⚠️ Images are collected solely for educational purposes and stored locally.  
> You can build your own dataset using `notebook/activity-crawling.ipynb`.

---

## 🛠️ Techniques

- Convolutional Neural Networks (CNN)  
- Transfer Learning with EfficientNetB0 / MobileNetV2  
- Strong image augmentation using `ImageDataGenerator`  
- Real-time classification via OpenCV  
- Metrics visualization (accuracy, loss curves)  
- Evaluation with confusion matrix and prediction overlay  

---

## 📁 Directory Structure

```bash

real-time-daily-activity-recognizer/
├── .gitignore                # Excludes checkpoints, temp files, dataset
├── experiment_logs/          # Experiment logs in Markdown
├── figures/                  # Accuracy/loss plots, confusion matrix images
├── images/                   # Crawled images organized by class (not included in repo)
├── notebook/                 # Jupyter Notebooks (training, crawling, inference)
├── README.md                 # Project description and instructions
└── requirements.txt          # Python dependencies

```
---

## 🚀 How to Run

```bash

1. **Install Dependencies**  
   pip install -r requirements.txt  

2. **Crawl Your Own Dataset (Optional)**  
   Edit and run: `notebook/activity-crawling.ipynb`  

3. **Train the Model**  
   Run notebook: `notebook/01_train_model.ipynb`  
   Check experiment logs in `experiment_logs/`  

4. **Run Inference (Webcam)**  
   Use: `notebook/03_realtime_inference.ipynb`  
   Or run a standalone script using `cv2.VideoCapture`  
   Press `q` to close the webcam window  

```

---

## 🚫 Limitations
- Dataset is relatively small and crawled from the web (quality and labeling errors may exist)  
- Limited to 8 predefined activity classes  
- Real-time inference may be sensitive to lighting, background, and camera quality  
- Not optimized for deployment on resource-constrained devices  

---

## 🔭 Next Steps
- Expand dataset with more balanced and diverse activity classes  
- Fine-tune additional architectures (EfficientNetV2, Vision Transformers)  
- Integrate real-time data augmentation and smoothing for more stable predictions  
- Deploy as a lightweight application (Streamlit / mobile demo)  

---

## 👤 Author
Maintained by [hojjang98](https://github.com/hojjang98)  
📅 Last updated: September 2025


