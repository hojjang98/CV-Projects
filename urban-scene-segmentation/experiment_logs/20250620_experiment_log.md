## ✅ 2025/06/20 Experiment Summary

### 🧾 What I Did Today

- Started training the **Image Segmentation** model for the "Urban Scene Segmentation" project  
- Implemented a baseline using **MobileNetV2 + U-Net-style decoder**  
- Preprocessed input images to 224×224 resolution  
- Used **categorical crossentropy** loss with `softmax` over multiple classes  
- Training was too slow, so the session was stopped early

### 📊 Observations

- Training speed was significantly slower than expected  
- Dataset loaded correctly (Cityscapes-like directory structure), but requires optimization  
- Model compiled and training started without errors, but not fully completed

### 💡 Insights

- May need to simplify the decoder or use a lighter backbone like EfficientNetB0  
- Reducing the input size (e.g., to 160×160) could improve speed  
- Data preprocessing and augmentation should be more efficient (e.g., via tf.data pipeline)

### 🎯 Next Steps

- Optimize model speed (lighter architecture or smaller inputs)  
- Run full training with callbacks like checkpoints and early stopping  
- Visualize segmentation outputs after each epoch  
- Try alternative architectures such as DeepLabV3+ or SegFormer
