# 🗑️ Garbage Classification

> **A Computer Vision Project for Multi-Class Waste Image Classification**  
> Build and evaluate deep learning models to automatically identify categories of garbage images.

---

## 🎯 Objectives
- Perform **EDA & preprocessing** on a garbage image dataset  
- Train a **baseline CNN** model for classification  
- Apply **transfer learning** (ResNet18, EfficientNetB0, etc.) for higher accuracy  
- Evaluate model performance with metrics and confusion matrices  

---

## 🧠 Methods
- **Dataset**: Garbage classification dataset (6–7 categories)  
- **Baseline Model**: Simple CNN (Conv → Pool → FC)  
- **Transfer Learning**: ResNet18 / EfficientNetB0 (fine-tuned on dataset)  
- **Evaluation**: Accuracy, precision/recall/F1, confusion matrix  

---

## 📊 Results (So Far)
- **Baseline CNN**: ~60% accuracy after 10 epochs  
- **Transfer Learning (ResNet18)**: ~80%+ accuracy achieved  
- Further improvements expected with **augmentation + regularization**  

---

## 📂 Project Structure

```bash

garbage-classification/
├── garbage_classification.ipynb  # Main notebook: EDA, training, evaluation
├── README.md                     # Project description

```
---

## 🚫 Limitations
- Dataset size is relatively small → risk of **overfitting**  
- Class distribution is **imbalanced**, which may bias predictions  
- Experiments so far are limited to **image classification only** (no detection/segmentation)  
- Results depend heavily on **transfer learning**; baseline model alone performs poorly  

---

## 🔭 Next Steps
- Add **data augmentation** (rotation, flip, color jitter)  
- Hyperparameter tuning with **Optuna**  
- Try **ensemble models** (Voting/Stacking of CNN + ResNet + EfficientNet)  
- Deploy lightweight model for **real-time demo**  

---

## 👤 Author
Maintained by [hojjang98](https://github.com/hojjang98)  
📅 Last updated: September 2025
