# Chapter 4 – CIFAR-10 Classification with CNN

This experiment builds on the baseline CIFAR-10 classification model from the textbook and incorporates several improvements.  
The goal was to better understand CNN training dynamics and to apply key enhancements while maintaining architectural simplicity.

---

## 🧠 Key Concepts

- Multi-class classification with softmax + categorical cross-entropy
- CNN architecture with Conv → ReLU → BatchNorm → MaxPooling → Dropout
- Data augmentation via `ImageDataGenerator`
- Use of `ReduceLROnPlateau` and `ModelCheckpoint` for stable training
- Evaluation through accuracy/loss plots

---

## 🗂 Dataset Overview

- **Source**: `keras.datasets.cifar10`
- **Image Size**: `32 x 32 x 3` (RGB)
- **Classes**: 10 (airplane, car, bird, cat, deer, dog, frog, horse, ship, truck)
- **Split**:
  - Train: 45,000  
  - Validation: 5,000  
  - Test: 10,000  

All images were normalized to zero mean and unit variance before training.

---

## 🏗 Model Architecture

```bash
Input: (3, 32, 32)

Conv2D(32) → ReLU → BatchNorm  
Conv2D(32) → ReLU → BatchNorm → MaxPool → Dropout(0.3)

Conv2D(64) → ReLU → BatchNorm  
Conv2D(64) → ReLU → BatchNorm → MaxPool → Dropout(0.4)

Conv2D(128) → ReLU → BatchNorm  
Conv2D(128) → ReLU → BatchNorm → MaxPool → Dropout(0.5)

GlobalAveragePooling2D  
Dense(10) → Softmax
```

Loss Function: categorical_crossentropy
Optimizer: Adam(lr=0.0001, decay=1e-6)
Epochs: 125
Batch Size: 128

## 📊 Training Performance

- **Best Validation Accuracy**: ~70.66%  
- **Final Test Accuracy**: ~71.12%  
- Learning rate dropped to `~2e-7` due to plateau monitoring

![Training Accuracy](https://raw.githubusercontent.com/hojjang98/CV-Projects/main/dl-chapter-notebooks/Chapter4/training_validation_acc.png)  
![Training Loss](https://raw.githubusercontent.com/hojjang98/CV-Projects/main/dl-chapter-notebooks/Chapter4/training_validation_loss.png)

---

## 📝 Observations

- Performance improved significantly over the original baseline (~67%)
- Validation curve closely followed training curve → good generalization
- BatchNorm and Dropout helped stabilize learning
- Model still limited by capacity — deeper networks or pretrained backbones could yield further improvements

---

## 💡 Reflection

This experiment started from the textbook's baseline CNN code and introduced key refinements:
- Increased filter sizes across blocks (32 → 64 → 128)
- Replaced Flatten with GlobalAveragePooling to reduce overfitting
- Applied learning rate scheduling via `ReduceLROnPlateau`

While the core architecture remained simple, these changes helped achieve more stable training and a ~4% boost in accuracy.  
The purpose was not to maximize accuracy, but to gain hands-on experience with training strategy and regularization techniques.

---

## 📁 Files

- `cifar10.ipynb` – Modified version of baseline code
- `training_validation_acc.png` – Accuracy curve
- `training_validation_loss.png` – Loss curve


