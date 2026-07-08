# AI-Powered Customer Churn Prediction System

## Project Overview

This project predicts whether a telecom customer is likely to churn using Machine Learning. It provides churn prediction, churn probability, risk level, and business recommendations through an interactive Streamlit web application.


## Features

- Customer Churn Prediction
- Churn Probability
- Risk Level Classification
- Business Recommendations
- Customer Summary
- Interactive Streamlit Dashboard
- End-to-End Machine Learning Pipeline


## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Joblib


## How to Run

1. Clone this repository.
2. Install the required libraries:

```bash
pip install -r requirements.txt
```

3. Run the Streamlit application:

```bash
streamlit run app.py
```


## Model Performance

| Model | Accuracy |
|--------|----------|
| Logistic Regression | 80.38% |
| Decision Tree | 75.20% |
| Random Forest | 79.46% |

The Logistic Regression model was selected as the final model based on its overall performance and balanced precision, recall, and F1-score.


## Future Improvements

- Add SHAP Explainability
- Deploy the application on Streamlit Community Cloud
- Add user authentication
- Store prediction history in a database
- Integrate LLM-based customer retention suggestions

## Author

**Shubha Sakshi**

B.Tech – Artificial Intelligence & Data Science