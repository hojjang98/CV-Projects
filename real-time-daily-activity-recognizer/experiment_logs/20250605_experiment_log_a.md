📅 **2025/06/06 Experiment Log — MobileNetV2 + Enhanced Data Augmentation**

**🧪 Experiment ID**: `exp_20250606_rgb_mobilenet_augmented`  
**🎯 Purpose**: Evaluate the impact of moderate data augmentation techniques on MobileNetV2's performance using RGB input, while keeping the base model frozen.

---

### ✅ Objective  
To test whether stronger image augmentation (rotation, shift, zoom, flip) can improve generalization without fine-tuning the pretrained MobileNetV2 backbone.

---

### ⚙️ Experiment Setup  
- **Input Format**: RGB (`color_mode='rgb'`)  
- **Model Architecture**: MobileNetV2 (`include_top=False`, `imagenet` weights, frozen)  
- **Augmentation**:
  - `rotation_range = 15`
  - `width_shift_range = 0.1`
  - `height_shift_range = 0.1`
  - `zoom_range = 0.1`
  - `horizontal_flip = True`
- **Loss / Optimizer**: Categorical Crossentropy / Adam (`lr=0.0003`, `β₁=0.85`, `β₂=0.995`)  
- **Batch Size**: 128  
- **Epochs**: 20  
- **Callbacks**:
  - `ModelCheckpoint` (save best only)  
  - `ReduceLROnPlateau`  
  - `EarlyStopping`  

---

### 📊 Results  
- **Best Validation Accuracy**: `0.5609` at Epoch `20`  
- **Observations**:  
  - Accuracy improved slightly compared to non-augmented baseline  
  - No signs of overfitting — loss curves smooth  
  - Plateau observed after ~15 epochs → indicates room for fine-tuning

---

### 📈 Training Curves  
<p align="center">
  <img src="https://github.com/hojjang98/CV-Projects/blob/main/real-time-daily-activity-recognizer/figures/20250605_experiment_a.png" width="600"/>
</p>

---

### 🔍 Insights  
- Augmentation helped generalization slightly  
- Still limited by frozen base model capacity  
- Suggests benefit from unfreezing top layers (fine-tuning)  
- MobileNetV2 still maintains stability under heavy augmentation

---

### 🧭 Next Step (Currently in Progress)

📅 **2025/06/06 - MobileNetV2 Fine-Tuning + Stronger Augmentation (Ongoing)**  
**Experiment ID**: `exp_20250606_rgb_mobilenet_finetune_augboost`

- **Unfreeze**: Last 20 layers of MobileNetV2  
- **Learning Rate**: `1e-5` (lowered for fine-tuning stability)  
- **Augmentation** (boosted):  
  - `brightness_range = [0.8, 1.2]`  
  - `shear_range = 10`  
  - Plus all previous transforms  
- **Epochs**: 25  
- **Batch Size**: 64

🎯 **Goal**: Boost validation accuracy and generalization through controlled fine-tuning and aggressive augmentation.

📤 **Expected Output**:  
- `figures/exp_20250606_finetune_mobilenet_augboost.png`  
- Updated best score & learning curve to be recorded
