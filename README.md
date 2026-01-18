# Customer Churn Prediction

##  Project Overview
Customer churn prediction is a critical problem for subscription-based businesses.  
This project focuses on predicting whether a customer is likely to churn using machine learning techniques and a neural network model.

The objective is to help organizations identify at-risk customers early and take proactive retention actions.

---

##  Problem Statement
Given historical customer data, the task is to predict whether a customer will **churn (leave the service)** or **remain loyal**.

This is treated as a **binary classification problem**.

---

##  Dataset Description
The dataset contains customer information such as:
- Demographic details
- Service subscriptions
- Usage patterns
- Billing and payment information
- Churn status

Categorical features were encoded and numerical features were scaled to prepare the data for modeling.

---

##  Exploratory Data Analysis
Exploratory Data Analysis (EDA) was performed to:
- Understand churn distribution
- Analyze relationships between customer behavior and churn
- Visualize key categorical and numerical features
- Identify patterns affecting customer retention

---

##  Data Preprocessing
- Handled missing values
- Converted categorical variables into numerical format
- Encoded binary features (Yes/No → 1/0)
- Prepared training and testing datasets

---

##  Model Architecture
- Artificial Neural Network (ANN)
- Input layer based on processed feature count
- Two hidden layers with ReLU activation
- Output layer with Sigmoid activation for probability prediction

---

##  Model Evaluation
The model was evaluated using:
- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix
- Classification Report visualizations

These metrics help assess model performance, especially for imbalanced class distributions.

---

##  Results
The model demonstrates strong performance in identifying customers at risk of churn.  
Evaluation metrics and visualizations provide meaningful insights into prediction quality and misclassification patterns.

---

##  Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- TensorFlow / Keras

---

##  How to Run the Project
1. Clone the repository
2. Open the notebook in Jupyter Notebook or Google Colab
3. Install the required dependencies
4. Run all cells to reproduce results

---

##  License
This project is licensed under the MIT License.

---
