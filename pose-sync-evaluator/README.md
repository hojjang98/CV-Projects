# 🕺 PoseSyncEvaluator

> **A Lightweight Dance Motion Alignment App Using 2D Poses, Cosine Similarity, and DTW**  
> Compare two dance motions frame-by-frame with pose-based similarity scoring and visual feedback.

---

## 🎯 Objectives
- Extract 2D human poses from videos using **MediaPipe**  
- Measure motion similarity with **Cosine Similarity** (per frame)  
- Perform temporal alignment using **FastDTW**  
- Provide quantitative scores and qualitative feedback via **Streamlit**  

---

## 🧠 Methods
- **Pose Extraction**: MediaPipe Pose (33 keypoints per frame)  
- **Similarity Metrics**: Cosine similarity (frame-level), FastDTW (sequence-level)  
- **Feedback**: Aggregated scores (cosine + DTW) → natural language feedback  
- **Visualization**: Cosine similarity curves, JSON score summary, Streamlit UI  

---

## 📊 Results
- Frame-level similarity and temporal alignment successfully measured  
- Demonstrated use case: **dance practice feedback**  
- Qualitative scoring (Excellent / Good / Needs Improvement / Poor) provides actionable guidance  
- Streamlit app supports simple and interactive testing with local `.npy` pose data  

---

## 📂 Project Structure

```bash

pose-sync-evaluator/
├── pose_data/                   # .npy pose keypoints (excluded in .gitignore)
├── 01_pose-sync-evaluator.ipynb # Notebook: data extraction + evaluation
├── pose_evaluator_app.py        # Streamlit app for similarity analysis
├── requirements.txt             # Dependencies
└── README.md

```

## 🚀 How to Run

``` bash

1. **Install dependencies**  
   pip install -r requirements.txt
2. **Prepare data**  
   - Extract frames from videos with `ffmpeg`  
   - Run `01_pose-sync-evaluator.ipynb` to generate `.npy` pose sequences  
   - Save results under:
     - `pose_data/ref/`  
     - `pose_data/user/`  
3. **Launch app**  
   streamlit run pose_evaluator_app.py
4. **Test in browser**
    Enter paths to reference and user pose folders (e.g., pose_data/gukmin, pose_data/user_trial_01)

```

## 🚫 Limitations
- Currently limited to **2D pose estimation** (MediaPipe)  
- Sensitive to frame alignment (requires trimming and consistent fps)  
- Small-scale prototype; not validated on large datasets  

---

## 🔭 Next Steps
- Extend to 3D pose estimation for richer evaluation  
- Add visualization of overlaid skeletons for qualitative comparison  
- Explore real-time webcam support for immediate feedback  
- Apply to broader use cases (exercise coaching, rehab monitoring)  

---

## 👤 Author
Maintained by [hojjang98](https://github.com/hojjang98)  
📅 Last updated: September 2025

