import os
import numpy as np
import streamlit as st
from fastdtw import fastdtw
from scipy.spatial.distance import cosine, euclidean

st.set_page_config(page_title="Pose Sync Evaluator", layout="centered")
st.title("Pose Sync Evaluator")
st.caption("Compare reference and user motion sequences with DTW and cosine similarity.")

# ------------------------------
# Helper functions
# ------------------------------

def load_pose_sequence(folder):
    """Load a sequence of pose frames stored as .npy files."""
    files = sorted(f for f in os.listdir(folder) if f.endswith(".npy"))
    return np.array([np.load(os.path.join(folder, f)) for f in files])

def compute_dtw_distance(seq1, seq2):
    """Compute DTW distance between two pose sequences."""
    seq1_flat = seq1.reshape(seq1.shape[0], -1)
    seq2_flat = seq2.reshape(seq2.shape[0], -1)
    distance, _ = fastdtw(seq1_flat, seq2_flat, dist=euclidean)
    return distance

def compute_cosine_scores(seq1, seq2):
    """Frame-by-frame cosine similarity scores."""
    scores = []
    for a, b in zip(seq1, seq2):
        score = 1 - cosine(a.flatten(), b.flatten())
        scores.append(score)
    return np.array(scores)

def summarize_scores(cosine_scores, dtw_distance, max_dtw=2000):
    """Summarize cosine and DTW into percentage-based scores."""
    cosine_score = np.mean(cosine_scores) * 100
    dtw_score = max(0, 100 * (1 - dtw_distance / max_dtw))
    total_score = 0.5 * cosine_score + 0.5 * dtw_score
    return {
        "Cosine Similarity Score": round(cosine_score, 2),
        "DTW Score": round(dtw_score, 2),
        "Total Score": round(total_score, 2)
    }

def generate_feedback(score):
    """Generate qualitative feedback from the total score."""
    if score >= 85:
        return "Excellent alignment"
    elif score >= 70:
        return "Good overall, with minor gaps"
    elif score >= 50:
        return "Some mismatch; more practice needed"
    else:
        return "Large mismatch; recheck the motion"


# ------------------------------
# Main App
# ------------------------------

st.subheader("Input Pose Folders")

ref_dir = st.text_input("Reference pose folder (e.g., pose_data/ref)")
usr_dir = st.text_input("User pose folder (e.g., pose_data/user)")

if ref_dir and usr_dir:
    try:
        ref_seq = load_pose_sequence(ref_dir)
        usr_seq = load_pose_sequence(usr_dir)

        # Match sequence lengths
        min_len = min(len(ref_seq), len(usr_seq))
        ref_seq, usr_seq = ref_seq[:min_len], usr_seq[:min_len]

        # Compute metrics
        dtw_dist = compute_dtw_distance(ref_seq, usr_seq)
        cosine_scores = compute_cosine_scores(ref_seq, usr_seq)
        results = summarize_scores(cosine_scores, dtw_dist)

        # Display results
        st.subheader("Similarity Scores")
        st.json(results)

        st.subheader("Cosine Similarity (per frame)")
        st.line_chart(cosine_scores)

        st.subheader("Feedback")
        st.write(generate_feedback(results["Total Score"]))

    except Exception as e:
        st.error(f"Error during processing: {e}")
else:
    st.info("Enter valid paths for both reference and user pose folders.")
