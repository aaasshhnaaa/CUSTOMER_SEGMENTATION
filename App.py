import streamlit as st
import pickle

# Load Model
model = pickle.load(open("kmeans_model(2).pkl", "rb"))

# Customer Labels
cluster_names = {
    0: "⭐ Regular Customer",
    1: "💎 Premium Customer",
    2: "🎯 Target Customer",
    3: "💰 Potential Customer",
    4: "🛒 Budget Customer"
}

# Title
st.title("🛍️ Customer Segmentation System")
st.write("Predict customer category using K-Means Clustering")

# Inputs
income = st.number_input(
    "Enter Annual Income (k$)",
    min_value=0.0,
    max_value=200.0,
    value=50.0
)

score = st.number_input(
    "Enter Spending Score (1-100)",
    min_value=0.0,
    max_value=100.0,
    value=50.0
)

# Prediction
if st.button("Predict Customer Segment"):

    prediction = model.predict([[income, score]])

    st.success(
        f"Customer Segment: {cluster_names[prediction[0]]}"
    )
