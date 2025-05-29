📅 **2025/05/29 Experiment Log — Real-Time Activity Recognizer**

**🧪 Experiment ID**: `exp_20250529_b2`  
**🎯 Purpose**: Reduce confusion between visually similar classes, especially `brushing_teeth` and `washing_face`.

---

### ✅ Objective
Address the issue where many other classes are misclassified as `brushing_teeth`, as observed in the previous confusion matrix.

---

### ⚙️ Experiment Setup
- **Backbone**: MobileNetV2 (pretrained, last 20 layers unfrozen)
- **Augmentation (global)**:
  - Increased intensity: `rotation=45°`, `shift=30%`, `zoom=0.4`, `brightness=[0.6, 1.4]`, `channel_shift=30`
- **Regularization**: `Dropout(0.5)`
- **Class Weighting**: Applied (`compute_class_weight`)
- **Optimizer/Loss**: Adam + `categorical_crossentropy`
- **Callbacks**: `ReduceLROnPlateau`, `EarlyStopping(patience=5)`
- **Epochs**: Max 20 (early stopped at 19)

---

### 📊 Results
- **Best Validation Accuracy**: _around_ `0.53~0.54`  
- **Observation**:
  - Validation accuracy remained stable and showed a smoother, longer upward trend
  - Train/val accuracy gap remained consistent → Overfitting reduced
  - Validation loss decreased more steadily than in the previous experiment

---

### 📈 Training Curves  
<p align="center">
  <img src="https://github.com/hojjang98/CV-Projects/blob/main/real-time-daily-activity-recognizer/figures/20250529_experiment_b.png" width="600"/>
</p>

---

### 🔍 Insights
- Augmentation strengthening across all classes appears to help with generalization
- `brushing_teeth`'s "black hole" effect may have been mitigated slightly
- Performance similar to or slightly better than `exp_20250529_b`, but learning behavior is healthier

---

### 📝 Next Steps
- [ ] Plot updated confusion matrix to assess improvement in `brushing_teeth` misclassifications
- [ ] Try `EfficientNetB0` or other stronger backbones
- [ ] Apply **class-specific augmentation** (e.g., heavier for `brushing_teeth`, `washing_face` only)
- [ ] Add more images for `washing_face` and `walking` via custom web crawling

---
