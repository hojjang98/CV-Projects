📅 **2025/06/06 Experiment Log — Fine-tuned MobileNetV2 + Strong Augmentation**

**🧪 Experiment ID**: `exp_20250606_rgb_mobilenet_finetune_augboost`  
**🎯 Purpose**: Evaluate the effectiveness of partial fine-tuning on MobileNetV2 combined with stronger augmentation to improve generalization and validation accuracy.

---

### ✅ Objective  
To test whether unfreezing the last layers of MobileNetV2 and applying aggressive augmentation improves validation accuracy beyond the baseline frozen model.

---

### ⚙️ Experiment Setup  
- **Input Format**: RGB (`color_mode='rgb'`)  
- **Model Architecture**: MobileNetV2  
  - `include_top=False`, `imagenet` weights  
  - Last **20 layers unfrozen** for fine-tuning  
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
- **Best Validation Accuracy**: `0.5371` at Epoch `19`  
- **Final Training Accuracy**: `0.6354`  
- **Observation**:  
  - Training accuracy continued to improve  
  - Validation accuracy plateaued around epoch 10 and fluctuated around `0.53`  
  - Suggests mild **overfitting** despite augmentation and low learning rate

---

### 📈 Training Curves  
<p align="center">
  <img src="https://github.com/hojjang98/CV-Projects/blob/main/real-time-daily-activity-recognizer/figures/20250605_experiment_b.png" width="600"/>
</p>

---

### 🔍 Insights  
- Fine-tuning with a small learning rate did not significantly outperform the frozen baseline  
- Aggressive augmentation helped delay overfitting but was not enough to push val accuracy higher  
- Model may be hitting its **capacity limit** or **data quality/class imbalance** may be affecting generalization  
- Stronger regularization (dropout), different optimizers, or learning rate schedules might help

---

### 🧭 Next Steps  
- [ ] Try **EfficientNetB0** or **ConvNeXt-Tiny** as alternative lightweight backbones  
- [ ] Apply **class-wise sampling or balancing** to handle imbalance  
- [ ] Introduce **Dropout layer** or **label smoothing** for regularization  
- [ ] Use **learning rate warm-up + cosine decay** for smoother fine-tuning
