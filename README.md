# CUSTOMER_SEGMENTATION



# Customer Segmentation using K-Means Clustering

## Overview

This project applies the K-Means Clustering algorithm to segment mall customers based on their annual income and spending behavior.

Customer segmentation helps businesses understand different customer groups and create targeted marketing strategies, improve customer retention, and increase revenue.

---

## Dataset

Dataset: Mall Customers Dataset

Features:

- CustomerID
- Gender
- Age
- Annual Income (k$)
- Spending Score (1-100)

For clustering, the following features were used:

- Annual Income (k$)
- Spending Score (1-100)

---

## Objectives

- Explore customer purchasing behavior.
- Identify meaningful customer groups.
- Determine the optimal number of clusters.
- Visualize customer segments.
- Generate business insights from the clusters.

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-Learn
- Jupyter Notebook

---

## Project Workflow

### 1. Data Loading

- Import dataset
- Check dataset shape
- View sample records

### 2. Data Exploration

- Missing value analysis
- Descriptive statistics
- Feature inspection

### 3. Data Visualization

- Scatter Plot
- Histograms
- Correlation Heatmap

### 4. Feature Selection

Selected features:

```python
Annual Income (k$)
Spending Score (1-100)
```

### 5. Finding Optimal K

Two methods were used:

#### Elbow Method

Measures Within Cluster Sum of Squares (WCSS) to determine the optimal number of clusters.

#### Silhouette Score

Evaluates cluster quality and separation.

### 6. K-Means Clustering

Model:

```python
KMeans(n_clusters=5)
```

### 7. Cluster Visualization

- Customer clusters plotted
- Centroids highlighted
- Cluster comparison performed

---

## Customer Segments Identified

### Cluster 1
Low Income - Low Spending

### Cluster 2
Low Income - High Spending

### Cluster 3
High Income - Low Spending

### Cluster 4
Medium Income - Medium Spending

### Cluster 5
High Income - High Spending

---

## Business Insights

### Most Valuable Customers

High Income - High Spending customers

Why?

- High purchasing power
- Strong spending behavior
- Potential for premium offerings

### Growth Opportunity

High Income - Low Spending customers

Why?

- Can afford more
- Respond well to personalized marketing

---

## Marketing Recommendations

| Customer Segment | Strategy |
|-----------------|----------|
| High Income - High Spending | Loyalty rewards and premium memberships |
| High Income - Low Spending | Personalized promotions |
| Low Income - High Spending | Discount offers and engagement campaigns |
| Low Income - Low Spending | Budget-friendly products |
| Medium Income - Medium Spending | Cross-selling and upselling |

---

## Advantages of K-Means

- Simple and easy to implement
- Fast and efficient
- Easy to visualize
- Works well on large datasets

---

## Limitations

- Requires predefined number of clusters
- Sensitive to outliers
- Assumes spherical clusters
- Results may vary with initialization

---

## Results

The analysis successfully identified five meaningful customer groups based on income and spending behavior.

These segments can help businesses:

- Improve customer targeting
- Increase customer retention
- Optimize marketing campaigns
- Enhance customer experience

---

## Future Improvements

- Use additional features such as Age and Gender
- Compare with Hierarchical Clustering
- Compare with DBSCAN
- Build an interactive dashboard
- Deploy as a web application

---

## Author

Aashna Mehta

Machine Learning Project – Customer Segmentation using K-Means Clustering
