# 🕺 PoseSyncEvaluator

> **A Lightweight Dance Motion Alignment App Using 2D Poses, Cosine Similarity, and DTW**  
> Compare two dance motions frame-by-frame with pose-based similarity scoring and visual feedback.

---

## 🎯 What This Project Does

This project evaluates how well two dance motions align by:

- Extracting 2D human poses from videos using **MediaPipe**
- Measuring motion similarity using **Cosine Similarity (per frame)**
- Performing **temporal alignment** with **FastDTW**
- Visualizing results and generating **natural language feedback** through **Streamlit**

---

## 🛠️ Techniques Used

- **MediaPipe Pose** (33 keypoints)
- **Cosine Similarity** (frame-level)
- **FastDTW** (sequence alignment)
- **Matplotlib** & **Streamlit** for visualization and interaction

---

## 📁 Project Structure

pose-sync-evaluator/
├── pose_data/ # Contains .npy pose keypoints (excluded from version control)
├── 01_pose-sync-evaluator.ipynb # Colab-based pipeline for pose extraction and evaluation
├── pose_evaluator_app.py # Streamlit app for similarity analysis
└── README.md


---

## 🚀 How to Try

# 📦 [1] Install dependencies (Colab or local)
pip install yt-dlp fastdtw mediapipe opencv-python-headless matplotlib scipy streamlit

# 🎥 [2] Download reference and user videos from YouTube
yt-dlp -f bestvideo+bestaudio --merge-output-format mp4 "https://www.youtube.com/watch?v=REF_VIDEO_ID" -o reference.mp4
yt-dlp -f bestvideo+bestaudio --merge-output-format mp4 "https://www.youtube.com/watch?v=USER_VIDEO_ID" -o user.mp4

# ✂️ [3] Trim videos to focus segment (adjust -ss as needed)
ffmpeg -ss 00:00:09 -i reference.mp4 -c copy reference_trimmed.mp4
ffmpeg -ss 00:00:11 -i user.mp4 -c copy user_trimmed.mp4

# 🖼️ [4] Extract frames from videos (2 fps)
mkdir -p frames/reference frames/user
ffmpeg -i reference_trimmed.mp4 -vf fps=2 frames/reference/frame_%04d.jpg
ffmpeg -i user_trimmed.mp4 -vf fps=2 frames/user/frame_%04d.jpg

# 🧍 [5] (Run notebook) Extract pose data from frames using MediaPipe
# 👉 Save .npy files into:
#     pose_data/gukmin/ (reference)
#     pose_data/user_trial_01/ (user)

# 🚀 [6] Launch Streamlit app
streamlit run pose_evaluator_app.py

# 🌐 [7] In your browser, enter:
#     pose_data/gukmin
#     pose_data/user_trial_01

## 💡 Applications

- 🕺 **Dance Practice Evaluation**  
  Compare a learner’s motion to a reference for training or feedback.

- 🧘 **Human Motion Alignment & Coaching**  
  Align physical therapy movements, exercise routines, or performance.

- 🧑‍🏫 **Educational Tools**  
  Provide intuitive feedback in dance or physical education classes.

- ⚡ **Lightweight Motion Evaluation**  
  Practical alternative to 3D pose-based scoring with minimal setup.

---

## 🔍 Background

This project was inspired by ideas from the paper:  
**"Unsupervised 3D Pose Estimation for Hierarchical Dance Video Recognition" (ICCV 2021)**

While the original paper focuses on **genre classification using 3D pose sequences**,  
this work explores **2D pose-based motion alignment and similarity scoring**  
with an emphasis on practical feedback and real-time usability.

---

## 🧠 Final Note

This project is part of my personal **Computer Vision portfolio**,  
highlighting my interest in **human motion analysis**, **pose estimation**, and  
**interactive feedback systems** grounded in visual AI.

> *Dance may be expressive — but even movement can be measured.*

