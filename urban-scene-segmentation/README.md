# 🏙️ Urban Scene Segmentation

This project performs pixel-wise semantic segmentation on urban street scenes using the **Cityscapes dataset**.  
The goal is to accurately identify objects such as **roads**, **cars**, **pedestrians**, **buildings**, and more from street-level images — a crucial step in building perception systems for self-driving cars.

---

## 📌 Project Overview

- **Task**: Semantic segmentation of urban scenes
- **Dataset**: Cityscapes (5,000 finely annotated images)
- **Model(s)**: U-Net, DeepLab v3+, SegFormer
- **Metric**: mIoU (mean Intersection over Union)
- **Goal**: Build a pixel-wise scene understanding pipeline for autonomous driving

---

## 🗂️ Project Structure

```bash
urban-scene-segmentation/
├── data/                # Raw & processed datasets
│   ├── raw/
│   └── processed/
├── notebooks/           # EDA, training, and experiments
│   ├── 01_eda.ipynb
│   ├── 02_unet_baseline.ipynb
│   └── 03_deeplab_experiment.ipynb
├── outputs/             # Model predictions & visualizations
│   ├── predictions/
│   └── visualizations/
├── src/                 # Dataset, model, training modules
│   ├── dataset.py
│   ├── model.py
│   ├── train.py
│   └── utils.py
├── requirements.txt     # Python dependencies
└── README.md
```
---

## 📂 Dataset & License

This project uses a publicly shared version of the **Cityscapes** dataset for semantic segmentation.

- **Unofficial Kaggle Source**: [Kaggle - Cityscapes by xiaose](https://www.kaggle.com/datasets/xiaose/cityscapes/data)
- **Original Dataset Reference**: [Cityscapes Official Site](https://www.cityscapes-dataset.com/)
- **License**: [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)  
  The dataset is used strictly for **non-commercial, educational, and research** purposes.

We do not redistribute the dataset directly. Please refer to the Kaggle link above to obtain the files.


