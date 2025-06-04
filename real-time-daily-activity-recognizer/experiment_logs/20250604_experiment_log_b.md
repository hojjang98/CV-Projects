📅 **2025/06/04 Experiment Log — Real-Time Activity Recognizer**

**🧪 Experiment ID**: `exp_20250604_gray_cnn_b`  
**🎯 Purpose**: Test performance of grayscale input using basic CNN architecture. Evaluate if grayscale input causes significant degradation in validation performance while keeping training stable.

---

### ✅ Objective  
Explore grayscale input's impact on validation accuracy when using a lightweight custom CNN. Compare against previous RGB-based baseline.

---

### ⚙️ Experiment Setup  
- **Input Format**: Grayscale (`color_mode='grayscale'`)  
- **Model Architecture**: Basic CNN  
  - `Conv2D(32) → MaxPooling`  
  - `Conv2D(64) → MaxPooling`  
  - `Flatten → Dense(128) → Dense(Softmax)`  
- **Augmentation**: None  
- **Loss / Optimizer**: Categorical Crossentropy / Adam (lr=0.0001)  
- **Callbacks**: `ModelCheckpoint` (save best only)  
- **Epochs**: 20  

---

### 📊 Results  
- **Best Validation Accuracy**: `0.5330` at Epoch `19`  
- **Observation**:  
  - **Validation accuracy plateaued early** (~0.53), no signs of overfitting  
  - **Training accuracy reached ~0.60**, indicating potential **underfitting**  
  - **Loss curves** were smooth and consistent, both train/val steadily decreased  
  - Model may lack capacity to extract sufficient features from grayscale input

---

### 📈 Training Curves  
<p align="center">
  <img src="https://github.com/hojjang98/CV-Projects/blob/main/real-time-daily-activity-recognizer/figures/20250604_experiment_b.png" width="600"/>
</p>

---

### 🔍 Insights  
- Grayscale input alone does not improve accuracy compared to RGB  
- Feature richness may have been reduced, limiting the model’s discriminative power  
- No overfitting observed, but capacity increase likely needed  
- Consider grayscale only if computational budget is very limited

---

### 🧭 Next Steps  
- [ ] Increase model capacity (add Conv layers, increase filters)  
- [ ] Repeat this architecture with RGB input for comparison  
- [ ] Try lightweight pretrained models (e.g., `MobileNet`, `EfficientNetB0`)  
- [ ] Incorporate image enhancement techniques for grayscale clarity (e.g., CLAHE)
