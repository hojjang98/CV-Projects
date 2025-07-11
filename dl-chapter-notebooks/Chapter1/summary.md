# Chapter 1 – Introduction to Computer Vision Systems

This chapter introduces the foundational concepts behind computer vision systems, their real-world applications, and how visual data can be processed and analyzed programmatically.  
Although no formal code implementation was required, I performed my own hands-on augmentation and transformation exercises using OpenCV and Matplotlib.

---

## 🧠 Key Concepts

- Components of a Computer Vision (CV) system
- Major application areas (e.g. surveillance, medical imaging, robotics)
- Step-by-step CV processing pipeline:  
  Image input → Preprocessing → Feature Extraction → Classification
- Understanding pixels, resolution, and color channels
- Types of image features (edges, gradients, contours, etc.)
- Classifier training: concept of feature-label mapping

---

## 🧪 My Experiment: Manual Image Transformations

Although the book did not provide a coding task, I implemented a set of classic image preprocessing techniques to reinforce the concepts covered.

### 🔧 Applied transformations:

- **Original**  
- **Gaussian Blur**  
- **Grayscale**  
- **Sobel Edge Detection**  
- **Canny Edge Detection**  
- **Color Inversion**  
- **Rotation (Tilted)**  

Each transformation was performed using basic OpenCV functions, mimicking the kind of preprocessing used before feature extraction or feeding into a classifier.

---

### 🖼 Output Samples

![Image Transformations]("https://github.com/hojjang98/CV-Projects/blob/main/dl-chapter-notebooks/Chapter1/dog_transformed.jpg")

> This grid shows how the same image can be interpreted very differently based on the applied transformation.  
> These techniques are fundamental to CV tasks like noise reduction, edge detection, and data augmentation for training models.

---

## 📝 Reflection

- Even without a model or training loop, image preprocessing alone shows how much can be done to enhance or abstract features from raw pixels.
- Visualizing different transformations helped solidify the **"CV pipeline"** concept: how to go from raw data to structured, useful features.
- I now better understand why CNNs often follow edge/gradient detection principles in their early layers.

---

## 📁 Files

- `summary.md` – This document
- `c01_basic_transforms.ipynb` – Code to generate transformations
- `dog_transformed.jpg` – Transformation output image

