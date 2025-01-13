

### Flight Price and Customer Satisfaction Prediction

---

## Overview
This project consists of two sub-projects designed to apply machine learning techniques in the **Travel and Tourism** and **Customer Experience** domains. It combines data preprocessing, machine learning model training, and interactive visualization using **Streamlit** with model tracking via **MLflow**.

---

## Project 1: Flight Price Prediction (Regression)

### **Skills Takeaway**
- Python, Streamlit, Machine Learning, Data Analysis, MLflow

### **Problem Statement**
Build an end-to-end system to predict flight ticket prices based on multiple factors, including departure time, source, destination, and airline type. 

### **Business Use Cases**
1. Helping travelers plan trips by predicting flight prices.
2. Assisting travel agencies with price optimization.
3. Enabling businesses to budget travel expenses.
4. Supporting airlines in optimizing pricing strategies.

### **Approach**
1. **Data Preprocessing**
   - Load and clean the dataset.
   - Feature engineering (e.g., calculate price per minute).
   - Convert date and time columns into usable formats.

2. **Model Training**
   - Perform EDA to uncover trends.
   - Train regression models (e.g., Linear Regression, Random Forest, XGBoost).
   - Integrate MLflow for experiment tracking and model registry.

3. **Streamlit App**
   - Build an app for visualizing flight trends and predicting prices.
   - Features: route, airline, and time-based filters.

---

## Project 2: Customer Satisfaction Prediction (Classification)

### **Skills Takeaway**
- Python, Machine Learning, Streamlit, Classification Models, MLflow

### **Problem Statement**
Develop a classification system to predict customer satisfaction levels based on feedback, demographics, and service ratings.

### **Business Use Cases**
1. Enhancing customer retention strategies.
2. Providing actionable insights for improving services.
3. Identifying target customer groups for marketing campaigns.

### **Approach**
1. **Data Preprocessing**
   - Handle missing values and encode categorical variables.
   - Normalize numerical features for consistent scaling.

2. **Model Training**
   - Perform EDA to identify feature relationships.
   - Train classification models (e.g., Logistic Regression, Random Forest, Gradient Boosting).
   - Log metrics (accuracy, F1-score) using MLflow.

3. **Streamlit App**
   - Interactive app to visualize satisfaction trends.
   - Input customer data and predict satisfaction levels.

---

## Streamlit Dashboard Features
- **Multi-Page Interface**:
  - Separate pages for Flight Price Prediction and Customer Satisfaction Prediction.
- **Interactive Visualizations**:
  - View trends for both projects with dynamic charts.
- **User Input Forms**:
  - Input flight or customer details for prediction.
- **Filters**:
  - Route, airline, and time filters for flight predictions.
  - Demographics and service-related filters for satisfaction predictions.

---

## Datasets
1. **Flight Price Dataset** (`Flight_Price.csv`):
   - Features: Airline, Source, Destination, Date of Journey, Route, etc.

2. **Customer Satisfaction Dataset** (`Passenger_Satisfaction.csv`):
   - Features: Gender, Customer Type, Age, Travel Type, Service Ratings, etc.

---

## Technical Highlights
- **MLflow**: Model tracking and experiment logging for both regression and classification tasks.
- **Streamlit**: Unified app for visualizing results and predictions.
- **Python**: Data preprocessing, feature engineering, and machine learning.

---


## Setup Instructions
### **Prerequisites**
- Python 3.8+
- MLflow and Streamlit installed
- Required Python libraries: `pandas`, `numpy`, `scikit-learn`, `matplotlib`, `seaborn`


### **Conclusion**
This dual-project system demonstrates real-world applications of machine learning in the travel and customer experience domains. By combining predictive modeling, MLflow tracking, and an interactive Streamlit interface, it offers robust tools for businesses and users alike.
