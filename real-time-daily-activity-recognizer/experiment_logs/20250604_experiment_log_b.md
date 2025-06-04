### 🧪 Experiment Log – 2025/06/04  
**📂 Project**: real-time-daily-activity-recognizer  
**🧪 Experiment**: CNN with Grayscale Input  
**🎯 Purpose**: Evaluate model performance with grayscale-converted input  
**🖼️ Plot Saved To**:  
`C:\Users\ghwns\HJ_git\CV-Projects\real-time-daily-activity-recognizer\figures\gray_experiment.png`

---

#### ✅ Experiment Details
- **Input Format**: Grayscale images (1 channel)
- **Model**: Simple CNN (Conv + MaxPooling + Dense layers)
- **Epochs**: 20  
- **Batch Size**: 128  
- **Optimizer**: Adam (`lr=0.0001`)  
- **Loss Function**: Categorical Crossentropy  
- **Metric**: Accuracy

---

#### 📊 Results Summary
- **Best Validation Accuracy**: `0.5330` at Epoch 19  
- **Overfitting**: ❌ No clear sign of overfitting (train/val gap moderate)  
- **Underfitting**: ✅ Likely underfitting  
  - Training accuracy plateaued at ~0.60  
  - Grayscale input may have reduced class-distinguishing features

---

#### 🔍 Key Takeaways
- Grayscale input did **not** improve performance  
- Model may lack capacity to learn from limited grayscale info  
- Using RGB may retain more discriminative features

---

#### 🔜 Next Steps
 Revert to RGB input to recover lost color information  
 Increase model depth / filter count (e.g., add more Conv layers, double filters)  
 Try transfer learning with MobileNet or similar architectures  
 Apply stronger data augmentation  
 Consider L2 regularization or Dropout to improve generalization
