# 🍽️ Food Image Classification

> *"I heard computer vision is trending these days..."*

This project started with that simple thought.  
While studying machine learning, I learned from my professor that the field of computer vision (CV) is rapidly gaining momentum and practical importance.  
Curious and excited, I decided to jump into it and explore image classification through this beginner-friendly project.

## 🎯 Project Goal

- Build a food image classifier using CNN and transfer learning.
- Gain hands-on experience with core CV tasks: preprocessing, augmentation, and evaluation.
- Understand the fundamentals of image classification in a practical, applied context.

## 📁 Dataset

- **Source**: Images were collected through Google Image crawling for educational and non-commercial use only.
- **Categories**: A custom subset of food-related categories including fruits, vegetables, and common dishes.
- **Availability**:  
  Image files are **excluded from this repository** to avoid copyright issues.

> ⚠️ All images used in this project were collected solely for educational purposes and remain stored locally.  
> If you want to build a similar dataset, refer to `food-image-crawling.ipynb`.

## 🔧 Techniques Used

- Convolutional Neural Networks (CNN)
- Transfer Learning (e.g., MobileNetV2)
- Image Augmentation (`ImageDataGenerator`)
- Evaluation: Accuracy, Confusion Matrix, Visual Predictions

## 🧱 Project Structure

```bash
food-image-classification/
├── .gitignore                        # Git ignore rules (e.g., images/, .h5 files)
├── .gitattributes                    # Git LFS / text file settings
├── figures/                          # Evaluation plots, confusion matrix, etc.
├── notebooks/                        # Jupyter notebooks for crawling & training
│   ├── 01_food-image-crawling.ipynb        # Web crawler using Selenium
│   └── 02_food-image-classification.ipynb  # CNN + Transfer Learning model training
├── README.md                         # Project overview
```


## 🚫 Notes on Image Usage

- All crawled image data is used strictly for **non-commercial, educational** purposes.
- To ensure proper copyright respect, these assets are **excluded from version control** using `.gitignore`.
- The dataset is **not redistributed**, but the tools to build it are provided in this repository.

---

Feel free to fork this repo and build your own food image classifier!  
Explore, visualize, model — and don’t forget to clean your data! 🍜🧼

## 📊 Final Results

- **Final Accuracy**: 61%
- **Macro F1-score**: 0.60
- **Best Classes**: `banana`, `kiwi`, `pineapple` (F1 > 0.84)
- **Weak Classes**: `capsicum`, `apple`, `corn`

> Model: MobileNetV2 (frozen base)  
> Optimizer: Adam + Learning Rate Scheduler  
> Epochs: 30 with EarlyStopping & ModelCheckpoint

## 🪜 What I Learned

This project wasn’t about chasing perfect accuracy —  
It was about building the entire computer vision workflow from scratch:

- Crawling and cleaning image data myself  
- Experimenting with CNNs and transfer learning  
- Understanding the impact of data size & augmentation  
- Respecting ethical boundaries (no redistribution)  
- Making tradeoffs between exploration and deadlines  

## 🧠 Key Files & Resources

| 📁 Resource | 🔗 Link |
|------------|--------|
| 📦 **Trained Model** (`best_model.h5`) | [Download from Google Drive](https://drive.google.com/file/d/1Qa55CoSG54oInE-lmYDbfJAyI1QJHcwd/view?usp=drive_link) |
| 📘 **GitHub Repository** | [🔗 food-image-classification](https://github.com/hojjang98/food-image-classification) |
| 📓 **Main Notebook (02)** – Model Training | [🔗 02_food-image-classification.ipynb](https://github.com/hojjang98/food-image-classification/blob/main/notebooks/food-image-classification.ipynb) |
| 📓 **Crawling Notebook (01)** – Image Scraper | [🔗 01_food-image-crawling.ipynb](https://github.com/hojjang98/food-image-classification/blob/main/notebooks/food-image-crawling.ipynb) |
| 📊 **Figures** – Accuracy, Loss, Confusion Matrix & Prediction Samples | [🔗 figures/](https://github.com/hojjang98/food-image-classification/tree/main/figures) |

> My biggest takeaway?  
> 📌 Better data beats better models — and deadlines teach focus.
