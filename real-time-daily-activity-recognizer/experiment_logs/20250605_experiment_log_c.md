📅 **2025/06/06 Experiment Log — MobileNetV2 Fine-Tuning + Dropout + Strong Augmentation**

**🧪 Experiment ID**: `exp_20250606_rgb_mobilenet_finetune_augdropout`  
**🎯 Purpose**: Investigate whether adding dropout improves validation accuracy and reduces overfitting in a fine-tuned MobileNetV2 model.

---

### ✅ Objective  
To regularize the model using Dropout after the global pooling layer, and observe if it enhances generalization when combined with strong augmentation techniques.

---

### ⚙️ Experiment Setup  
- **Input Format**: RGB (`color_mode='rgb'`)  
- **Model Architecture**: MobileNetV2 (last 20 layers unfrozen)  
  - `GlobalAveragePooling2D → Dropout(0.5) → Dense(Softmax)`  
- **Augmentation**:
  - `rotation_range = 15`  
  - `width/height shift = 0.1`  
  - `zoom_range = 0.1`  
  - `brightness_range = [0.8, 1.2]`  
  - `shear_range = 10`  
  - `horizontal_flip = True`
- **Loss / Optimizer**: Categorical Crossentropy / Adam (`lr=1e-5`)  
- **Batch Size**: 64  
- **Epochs**: 25  
- **Callbacks**:
  - `ModelCheckpoint` (save best only)  
  - `ReduceLROnPlateau`  
  - `EarlyStopping`

---

### 📊 Results  
- **Best Validation Accuracy**: `0.5437` at Epoch `25`  
- **Final Train Accuracy**: `0.5084`  
- **Observation**:
  - Validation accuracy consistently improved across epochs  
  - Gap between train and val accuracy was minimal, with val accuracy higher at several points  
  - Strong evidence of **reduced overfitting** thanks to dropout

---

### 📈 Training Curves  
<p align="center">
  <img src="https://github.com/hojjang98/CV-Projects/blob/main/real-time-daily-activity-recognizer/figures/20250605_experiment_c.png" width="600"/>
</p>

---

### 🔍 Insights  
- Dropout reduced training accuracy slightly but **increased generalization**  
- Validation accuracy overtook training accuracy for most of the epochs  
- This trade-off is desirable in small or imbalanced datasets  
- Compared to previous fine-tuning-only results, performance is slightly better and much more stable

---

### 🧭 Next Steps  
- [ ] Try **label smoothing** to further control overconfident predictions  
- [ ] Explore **EfficientNetB0** to test alternative lightweight backbones  
- [ ] Analyze **confusion matrix** to find class-specific bottlenecks  
- [ ] Optionally reduce augmentation to see if Dropout alone helps
