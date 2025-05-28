# 🧪 Experiment Log: Real-Time Daily Activity Recognizer

## 📅 2025/05/28

### ✅ Goal
Rebuild the image classification pipeline using transfer learning after the initial MobileNetV2 code broke. Start clean with structured experiments, aiming to exceed 40% validation accuracy.

---

### 🔬 Experiment 01: Baseline MobileNetV2 (Transfer Learning)

- **Model**: MobileNetV2 (pretrained on ImageNet)
- **Frozen Base**: ✅ Yes
- **Custom Head**:
  - `GlobalAveragePooling2D`
  - `Dropout(0.5)`
  - `Dense(num_classes, activation='softmax')`
- **Input Shape**: (224, 224, 3)
- **Optimizer**: Adam
- **Callbacks**: `ReduceLROnPlateau`
- **Epochs**: 10
- **Batch Size**: 32

---

### 📊 Results

- **Best Val Accuracy**: 🏆 **0.5518** at **Epoch 7**
- **Train/Val Accuracy Gap**: Small → generalization is solid
- **Val Loss**: Decreasing steadily; slight noise but overall stable
- **No signs of overfitting**

---

### 📷 Screenshot
![val_accuracy_plot](https://github.com/hojjang98/CV-Projects/tree/main/real-time-daily-activity-recognizer/figures/)

---

### 🧠 Insights

- Transfer learning with MobileNetV2 is significantly more effective than custom CNN blocks.
- Dropout(0.5) works well here because the backbone is robust enough.
- 224x224 input resolution has improved representational power compared to 128x128.

---

### 🎯 Next Steps

- [ ] Save the current model: `model.save("mobilenetv2_baseline_055.h5")`
- [ ] Add fine-tuning (unfreeze last 20 layers) to push beyond 60% accuracy
- [ ] Evaluate on test set or unseen samples
- [ ] Visualize predictions (single image + confusion matrix)

---
