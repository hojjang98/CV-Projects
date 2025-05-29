📅 **2025/05/29 Experiment Log — Real-Time Activity Recognizer**

**✅ Objective**  
Improve validation performance of the image classification model using transfer learning and fine-tuning.

**🧪 Experiment Setup**  
- **Backbone**: MobileNetV2 (pretrained on `imagenet`, last 20 layers unfrozen for fine-tuning)  
- **Augmentation**: Rotation ±30°, width/height shift ±20%, channel shift, brightness range  
- **Regularization**: `Dropout(0.5)`  
- **Class Imbalance Handling**: Applied `class_weight` to upweight underrepresented class (`walking`)  
- **Training Strategy**: `ReduceLROnPlateau` + `EarlyStopping(patience=5)`  
- **Epochs**: Max 20 (early stopped at epoch 13)

**📊 Results**  
- **Best Validation Accuracy**: `0.5370 @ Epoch 9`  
- **Train Accuracy**: Steady increase to above `0.65`  
- **Validation Accuracy**: Relatively stable with no severe overfitting

**📈 Plots**  
<p align="center">
  <img src="https://github.com/hojjang98/CV-Projects/blob/main/real-time-daily-activity-recognizer/figures/20250529_experiment_a.png" width="600"/>
</p>

**🔍 Insights**  
- Fine-tuning significantly improved performance (+10%p compared to frozen backbone)  
- Still a noticeable gap between train and validation accuracy → consider more diverse data  
- Class weighting showed positive effect on imbalance correction

**📝 Next Steps**  
- [ ] Try different backbones: `EfficientNetB0`, `ResNet50`, etc.  
- [ ] Introduce advanced regularization: `MixUp`, `Label Smoothing`  
- [ ] Analyze confusion matrix for class-wise improvement opportunities
