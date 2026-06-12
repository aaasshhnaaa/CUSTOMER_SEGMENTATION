import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from sklearn.cluster import KMeans

st.set_page_config(page_title="Customer Segmentation K-Means", layout="wide")

st.title("Customer Segmentation Using K-Means Clustering")

df = pd.read_csv("Mall_Customers.csv")

st.subheader("Dataset Preview")
st.dataframe(df.head(10))

st.subheader("Dataset Shape")
st.write(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")

st.subheader("Missing Values")
st.dataframe(df.isnull().sum().reset_index().rename(columns={"index": "Column", 0: "Missing Values"}))

st.subheader("Descriptive Statistics")
st.dataframe(df.describe())

st.subheader("Scatter Plot: Annual Income vs Spending Score")
fig1, ax1 = plt.subplots()
sns.scatterplot(data=df, x='Annual Income (k$)', y='Spending Score (1-100)', ax=ax1)
st.pyplot(fig1)

X = df[['Annual Income (k$)', 'Spending Score (1-100)']]

wcss = []
for k in range(1, 11):
    model = KMeans(n_clusters=k, init='k-means++', random_state=42)
    model.fit(X)
    wcss.append(model.inertia_)

st.subheader("Elbow Method")
fig2, ax2 = plt.subplots()
ax2.plot(range(1, 11), wcss, marker='o')
ax2.set_xlabel("Number of Clusters (K)")
ax2.set_ylabel("WCSS")
ax2.set_title("Elbow Curve")
st.pyplot(fig2)

k = st.slider("Select number of clusters", 2, 10, 5)

kmeans = KMeans(n_clusters=k, init='k-means++', random_state=42)
df['Cluster'] = kmeans.fit_predict(X)

st.subheader("Clustered Data")
st.dataframe(df.head(10))

st.subheader("Cluster Visualization")
fig3, ax3 = plt.subplots(figsize=(8, 6))
sns.scatterplot(
    data=df,
    x='Annual Income (k$)',
    y='Spending Score (1-100)',
    hue='Cluster',
    palette='Set1',
    s=100,
    ax=ax3
)

centers = kmeans.cluster_centers_
ax3.scatter(centers[:, 0], centers[:, 1], c='black', s=300, marker='X', label='Centroids')
ax3.legend()
st.pyplot(fig3)

st.subheader("Cluster Centers")
centers_df = pd.DataFrame(centers, columns=['Annual Income (k$)', 'Spending Score (1-100)'])
st.dataframe(centers_df)

