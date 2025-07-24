# 🕺 PoseSyncEvaluator: 2D Dance Alignment with Pose & DTW

> *"Are we really dancing the same?"*

🚧 **This project is a Work In Progress (WIP)** 🚧  
🟢 Currently developed and tested in **Google Colab**

This project is inspired by ideas from the paper:  
**“Unsupervised 3D Pose Estimation for Hierarchical Dance Video Recognition” (ICCV 2021)**  
While the original paper focuses on 3D poses and genre classification, I explored how similar ideas can be applied to 2D pose-based dance alignment and motion scoring.

---

## 🎯 Project Goal

- Extract 2D human poses from dance videos using MediaPipe
- Align movements with DTW (Dynamic Time Warping)
- Quantify similarity using cosine scores + temporal alignment
- Visualize and interpret how well two dances match

---

## 📁 Dataset

- **Source**: YouTube dance clips (for educational purposes only)
- **Types**: One reference video, one user performance
- **Usage**: Stored locally for evaluation. Not included in this repo.

> ⚠️ All videos and frame data are excluded from version control via `.gitignore`.

---

## 🔧 Techniques Used

- MediaPipe Pose (33 keypoints)
- Cosine Similarity (per frame)
- FastDTW (alignment)
- Visualization: similarity curves & DTW path

---

## 📊 Sample Output

- Frame-by-frame cosine similarity plot  
- DTW alignment map (reference vs. user)  
- Overall matching score (frame + motion)

---

## 💭 Research Direction

This project is part of my ongoing effort to build a pose-based motion evaluation system.  
It is also the **first module in my broader `cv-projects` collection**, which will include multiple computer vision experiments focused on motion, feedback, and real-time interaction.

Planned extensions include:

- Real-time similarity measurement from webcam or video stream  
- Visual feedback overlays for training or dance practice  
- Human-centered feedback systems for intuitive pose guidance  
- Lightweight alternatives to 3D motion scoring for practical deployment

Eventually, I aim to develop this into a research prototype or paper proposal.

---

## 🧠 Key Notebook

| 📓 Notebook | 🔗 Link |
|------------|--------|
| Main Pipeline | `01_pose-sync-evaluator.ipynb` |

---

## 🧪 Environment

This project is developed and tested on **Google Colab**,  
with the following setup:

- Python 3.11  
- `yt-dlp`, `opencv-python-headless`, `mediapipe`, `fastdtw`  
- Notebook includes YouTube video download + frame extraction + pose processing

> For local execution, ensure you install all dependencies and adjust paths accordingly.

---

> Dance may be expressive, but even movement can be measured.  
> This is a WIP project — and just the beginning of my `cv-projects` journey. 🔄
