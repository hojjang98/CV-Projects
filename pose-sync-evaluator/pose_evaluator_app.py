import os
import numpy as np
import streamlit as st
from fastdtw import fastdtw
from scipy.spatial.distance import cosine, euclidean
import matplotlib.pyplot as plt

st.set_page_config(page_title="Pose Sync Evaluator", layout="centered")
st.title("Pose Sync Evaluator")
st.caption("Measure motion similarity between a reference and a user using DTW and cosine similarity.")

# Helper functions


def load_pose_sequence(folder):
    files = sorted(f for f in os.listdir(folder) if f.endswith(".npy"))
    return np.array([np.load(os.path.join(folder, f)) for f in files])

def compute_dtw_distance(seq1, seq2):
    seq1_flat = seq1.reshape(seq1.shape[0], -1)
    seq2_flat = seq2.reshape(seq2.shape[0], -1)
    distance, _ = fastdtw(seq1_flat, seq2_flat, dist=euclidean)
    return distance

def compute_cosine_scores(seq1, seq2):
    scores = []
    for a, b in zip(seq1, seq2):
        a_flat = a.flatten()
        b_flat = b.flatten()
        score = 1 - cosine(a_flat, b_flat)
        scores.append(score)
    return np.array(scores)

def summarize_scores(cosine_scores, dtw_distance, max_dtw=2000):
    cosine_score = np.mean(cosine_scores) * 100
    dtw_score = max(0, 100 * (1 - dtw_distance / max_dtw))
    total_score = 0.5 * cosine_score + 0.5 * dtw_score
    return {
        "Cosine Similarity Score": round(cosine_score, 2),
        "DTW Score": round(dtw_score, 2),
        "Total Score": round(total_score, 2)
    }

def generate_feedback(score):
    if score >= 85:
        return "Excellent alignment."
    elif score >= 70:
        return "Good job. Some improvement needed."
    elif score >= 50:
        return "Noticeable mismatch. Keep practicing."
    else:
        return "Significant mismatch. Revisit the motion."


# Main app

st.subheader("Select Input Folders")

ref_dir = st.text_input("Reference pose folder (e.g., pose_data/gukmin)")
usr_dir = st.text_input("User pose folder (e.g., pose_data/user_trial_01)")

if ref_dir and usr_dir:
    try:
        ref_seq = load_pose_sequence(ref_dir)
        usr_seq = load_pose_sequence(usr_dir)

        min_len = min(len(ref_seq), len(usr_seq))
        ref_seq = ref_seq[:min_len]
        usr_seq = usr_seq[:min_len]

        dtw_dist = compute_dtw_distance(ref_seq, usr_seq)
        cosine_scores = compute_cosine_scores(ref_seq, usr_seq)
        results = summarize_scores(cosine_scores, dtw_dist)

        st.subheader("Similarity Scores")
        st.json(results)

        st.subheader("Cosine Similarity per Frame")
        st.line_chart(cosine_scores)

        st.subheader("Feedback")
        st.success(generate_feedback(results["Total Score"]))

    except Exception as e:
        st.error(f"Error while processing sequences: {e}")
else:
    st.info("Enter valid paths to both reference and user pose folders.")
