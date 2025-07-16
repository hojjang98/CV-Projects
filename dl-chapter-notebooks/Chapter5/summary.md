# Chapter 5 – Advanced CNN Architectures on CIFAR-10

This chapter explores several **classical convolutional neural network architectures**, ranging from LeNet to ResNet, and compares their performance on the CIFAR-10 dataset.  
The goal was to gain practical experience with well-known CNN models and observe how depth, architectural innovations, and design choices affect classification performance.

---

## 🧠 Key Concepts

- Comparative benchmarking of LeNet, AlexNet, VGG, and ResNet architectures
- Observing how different designs handle small-resolution images (32x32)
- Hands-on implementation and training of each model
- Importance of residual connections and depth vs. parameter efficiency

---

## 🗂 Dataset Overview

- **Source**: `keras.datasets.cifar10`
- **Image Size**: `32 x 32 x 3` (RGB)
- **Classes**: 10 (airplane, car, bird, cat, deer, dog, frog, horse, ship, truck)
- **Split**:
  - Train: 45,000  
  - Validation: 5,000  
  - Test: 10,000  

All images were normalized using standard normalization (mean = 0, std = 1).

---

## 🏗 Compared Architectures

| Model     | Key Features                                      | Params (Approx.) | Notes |
|-----------|---------------------------------------------------|------------------|-------|
| LeNet-5   | 2 Conv + 3 FC layers                               | ~60K             | Early CNN, originally for MNIST |
| AlexNet   | ReLU, Dropout, 5 Conv + 3 FC layers                | ~60M             | First deep CNN to win ImageNet |
| VGG-16    | Stacked 3x3 Convs, no fancy tricks                 | ~138M            | Simple yet powerful |
| ResNet-18 | Residual connections, deeper network               | ~11M             | Enables stable deep learning |

Each model was adapted to fit CIFAR-10’s input size and trained from scratch.

---

## ⚙️ Training Setup

- Optimizer: Adam (lr=0.0001)
- Epochs: 100–125 (depending on convergence)
- Batch Size: 128
- Loss Function: Categorical Crossentropy
- Data Augmentation: Random Flip, Rotation, Width/Height Shift
- EarlyStopping + ReduceLROnPlateau applied

---

## 📊 Results (Preliminary)

| Model     | Best Val Accuracy | Test Accuracy (Approx.) |
|-----------|-------------------|--------------------------|
| LeNet     | ~57%              | ~56%                     |
| AlexNet   | ~67%              | ~66%                     |
| VGG-16    | ~73%              | ~72%                     |
| ResNet-18 | ~81%              | ~80%                     |

📌 *Note: All models were trained under the same preprocessing and augmentation pipeline for fair comparison.*

---

## 📝 Observations

- ResNet-18 outperformed others by a significant margin, thanks to residual learning.
- VGG-16 showed strong performance despite its simplicity, but training took longer.
- AlexNet’s larger number of parameters didn't guarantee better accuracy.
- LeNet underperformed due to shallow depth and outdated architecture.

---

## 💡 Reflection

This chapter provided hands-on practice with legendary CNN architectures.  
Key takeaways include:
- Deep networks benefit from residual connections and normalization
- Simplicity (like VGG) can still be effective with proper tuning
- Model architecture must be chosen based on task constraints (speed vs. accuracy)

In the next chapter, I plan to explore transfer learning using pretrained models to go beyond training from scratch.

---

## 📁 Files

- `lenet_cifar10.ipynb`  
- `alexnet_cifar10.ipynb`  
- `vgg16_cifar10.ipynb`  
- `resnet18_cifar10.ipynb`  
- Training plots: `acc_loss_comparison.png`

