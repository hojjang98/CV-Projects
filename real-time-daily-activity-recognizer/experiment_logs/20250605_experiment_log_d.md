📅 **2025/06/06 Experiment Log — EfficientNetB0 + Dropout + Strong Augmentation**

**🧪 Experiment ID**: `exp_20250606_rgb_efficientnetb0_dropout_aug`  
**🎯 Purpose**: Test whether switching to EfficientNetB0 improves performance over MobileNetV2 when combined with strong augmentation and dropout.

---

### ✅ Objective  
To evaluate EfficientNetB0’s performance as a lightweight backbone on the real-time activity recognition dataset, using enhanced data augmentation and dropout for regularization.

---

### ⚙️ Experiment Setup  
- **Input Format**: RGB (`color_mode='rgb'`)  
- **Image Size**: `160 x 160`  
- **Model**: EfficientNetB0 (`include_top=False`, `imagenet` weights)  
- **Base model**: Fully frozen  
- **Augmentation**:
  - `rotation_range = 15`  
  - `width/height shift = 0.1`  
  - `zoom_range = 0.1`  
  - `brightness_range = [0.8, 1.2]`  
  - `shear_range = 10`  
  - `horizontal_flip = True`
- **Dropout**: `Dropout(0.5)` after `GlobalAveragePooling2D`
- **Loss / Optimizer**: Categorical Crossentropy / Adam (`lr=1e-4`)  
- **Batch Size**: 64  
- **Epochs**: 25  
- **Callbacks**:
  - `ModelCheckpoint`  
  - `ReduceLROnPlateau`  
  - `EarlyStopping`

---

### 📊 Results  
- **Best Validation Accuracy**: `0.5680` at Epoch `23`  
- **Final Train Accuracy**: `0.5272`  
- **Observation**:
  - Validation accuracy was consistently higher than training accuracy  
  - Very stable learning curves, no overfitting detected  
  - This configuration achieved the best result so far in the project

---

### 📈 Training Curves  
<p align="center">
  <img src="https://github.com/hojjang98/CV-Projects/blob/main/real-time-daily-activity-recognizer/figures/20250605_experiment_d.png" width="600"/>
</p>

---

### 🔍 Insights  
- EfficientNetB0 outperformed MobileNetV2 in both stability and accuracy  
- Dropout regularization + aggressive augmentation provided excellent generalization  
- Model is likely under-capacity rather than overfitting — fine-tuning may improve further

---

### 🧭 Next Steps  
- [ ] Unfreeze top N layers for **selective fine-tuning**  
- [ ] Increase image size to `192x192` and evaluate performance gain  
- [ ] Apply **label smoothing** to further stabilize predictions  
- [ ] Visualize confusion matrix again to reassess class-specific performance
