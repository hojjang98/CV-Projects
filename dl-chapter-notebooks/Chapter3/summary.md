# Chapter 3 – CNN Implementation: Cat vs. Dog Classification

This experiment implements a simple Convolutional Neural Network (CNN) to classify cats and dogs using the [Oxford-IIIT Pet Dataset](https://www.robots.ox.ac.uk/~vgg/data/pets/).  
The goal is to practice building a full image classification pipeline: preprocessing, model definition, training, and evaluation.

---

## 🧠 Key Concepts

- CNN architecture: Convolution → ReLU → Pooling → Fully Connected
- Binary classification with sigmoid activation + BCELoss
- Confusion matrix analysis for class-wise evaluation
- Visual inspection of correct vs. incorrect predictions

---

## 🗂 Dataset Overview

- **Source**: `torchvision.datasets.OxfordIIITPet`
- **Input size**: RGB images resized to `64 x 64`
- **Filtered for binary classification**:
  - Label `≤ 4` → Cat (`0`)
  - Label `> 4` → Dog (`1`)
- **Total Samples**:  
  - Cats ≈ 500  
  - Dogs ≈ 3180

---

## 🏗 Model Architecture

```bash
Input: (3, 64, 64)

Conv2d(3, 16, kernel_size=3, padding=1)
→ ReLU
→ MaxPool2d(2)

Conv2d(16, 32, kernel_size=3, padding=1)
→ ReLU
→ MaxPool2d(2)

→ Flatten
→ Linear(8192, 128)
→ ReLU
→ Linear(128, 1)
→ Sigmoid
```


- **Loss Function**: `BCELoss()`
- **Optimizer**: `Adam(lr=0.001)`
- **Epochs**: 5  
- **Batch Size**: 32

---

## 📊 Training Performance

| Epoch | Loss   | Accuracy |
|-------|--------|----------|
| 1     | 0.4096 | 0.8636   |
| 2     | 0.3930 | 0.8641   |
| 3     | 0.3859 | 0.8641   |
| 4     | 0.3684 | 0.8641   |
| 5     | 0.3564 | 0.8660   |

![Training Graphs]("https://github.com/hojjang98/CV-Projects/blob/main/dl-chapter-notebooks/Chapter3/training_loss_plot.png")

---

## 🔍 Confusion Matrix

Model shows strong bias toward predicting dogs correctly, but often misclassifies cats as dogs.

            Predicted
        |  Cat  |  Dog
True ---------------------
Cat     | 41    | 459
Dog     | 19    | 3161


![Confusion Matrix]("https://github.com/hojjang98/CV-Projects/blob/main/dl-chapter-notebooks/Chapter3/Confusion_Matrix.png")

---

## 🖼 Sample Predictions

### ✅ Correct Predictions

![Correct Predictions]("https://github.com/hojjang98/CV-Projects/blob/main/dl-chapter-notebooks/Chapter3/correct_predictions.png")

*GT: Ground Truth, Pred: Model Prediction*

---

## 📝 Observations

- Overall accuracy ~86.6%, but extremely imbalanced.
- Dog classification is very accurate (3161/3180).
- Cat classification performs poorly (only 41/500 correct).
- Likely caused by:
  - Class imbalance (more dog images)
  - Less intra-class variation for cats (only 5 classes)

---

## 💡 Reflection

This experiment helped reinforce:
- How convolution and pooling layers process image features
- How sigmoid + BCELoss work for binary classification
- Why class imbalance matters, especially for real-world deployment
- Importance of visualization (confusion matrix, prediction samples)

> **Note**:  
> The goal of this experiment was not to optimize performance, but to implement a full CNN pipeline and understand its components in practice.  
> Therefore, no model tuning, data balancing, or architectural refinement was applied beyond the basic structure.

This was a hands-on, exploratory exercise focused on learning through implementation.

---

## 📁 Files

- `cnn_catdog_train.py` – Training code
- `chapter3.ipynb` – Jupyter notebook version
- `README.md` – This document
- Images: `training_plot.png`, `confusion_matrix.png`, `correct_predictions.png`


