📅 **2025/06/04 Experiment Log — Real-Time Activity Recognizer**

**🧪 Experiment ID**: `exp_20250604_gray_cnn_a`  
**🎯 Purpose**: Evaluate grayscale input with a custom CNN architecture to reduce model size and complexity while maintaining baseline performance.

---

### ✅ Objective  
Test whether grayscale transformation and a custom-built CNN can provide comparable validation performance, while reducing computation and avoiding overfitting.

---

### ⚙️ Experiment Setup  
- **Input Format**: Grayscale (`color_mode='grayscale'`)  
- **Model Architecture**: Custom CNN  
  - `Conv2D(32) → MaxPooling`  
  - `Conv2D(64) → MaxPooling`  
  - `Conv2D(128) → MaxPooling`  
  - `Flatten → Dropout(0.5) → Dense(128) → Dense(Softmax)`  
- **Augmentation**: `rotation=20°`, `zoom=0.2`, `shift=10%`, `horizontal_flip=True`  
- **Loss / Optimizer**: Categorical Crossentropy / Adam  
- **Callbacks**: `ReduceLROnPlateau`, `EarlyStopping(patience=5)`  
- **Class Weighting**: Applied (`compute_class_weight`)  
- **Epochs**: Max 20 (early stopped at 19)  

---

### 📊 Results  
- **Best Validation Accuracy**: `0.2678` at Epoch `18`  
- **Observation**:  
  - Accuracy was **similar to RGB model**, although slightly lower  
  - **Loss dropped steadily**, showing stable learning  
  - No clear signs of overfitting, but **underfitting likely** — overall performance plateaued early

---

### 📈 Training Curves  
<p align="center">
  <img src="https://github.com/hojjang98/CV-Projects/blob/main/real-time-daily-activity-recognizer/figures/20250604_gray_cnn_a.png" width="600"/>
</p>

---

### 🔍 Insights  
- Grayscale input can be viable, especially with constrained resources  
- Accuracy stayed around ~0.26, suggesting feature extraction was limited  
- Loss convergence was smooth and regularization appeared effective  
- **Likely underfitting** — model capacity or grayscale representation may be limiting factors

---

### 🧭 Next Steps 
- [ ] Increase model depth or filters (e.g., add more Conv layers or wider kernels)  
- [ ] Compare against same architecture with RGB input to isolate grayscale effect  
- [ ] Use smaller pretrained backbone again? (e.g., `EfficientNetB0`, `MobileNetV3`) on grayscale (converted to 3-channel)  
- [ ] Try contrast enhancement (e.g., CLAHE) during preprocessing to boost grayscale detail
