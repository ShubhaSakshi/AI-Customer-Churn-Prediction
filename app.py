import streamlit as st
import pandas as pd
import joblib



pipeline = joblib.load("customer_churn_pipeline.pkl")

preprocessor = pipeline.named_steps["preprocessor"]
model = pipeline.named_steps["model"]

st.set_page_config(
    page_title="AI Customer Churn Prediction",
    page_icon="📊",
    layout="wide"
)

st.title("📊 AI-Powered Customer Churn Prediction System")

st.write(
    "Predict whether a telecom customer is likely to churn using a Machine Learning model."
)

# ---------------- Sidebar ----------------

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Select a Page",
    ["Home", "Prediction"]
)


# ---------------- Home Page ----------------

if page == "Home":

    st.header("Welcome")

    st.write(
        """
        Welcome to the AI-Powered Customer Churn Prediction System.

        Use the Prediction page to check whether a customer is likely to churn.
        """
    )

    # ---------------- Prediction Page ----------------

elif page == "Prediction":

    st.header("Customer Prediction")

    col1, col2 = st.columns(2)

    with col1:
       
       gender = st.selectbox(
        "Gender",
        ["Female", "Male"]
     )

       senior_citizen = st.selectbox(
        "Senior Citizen",
        [0, 1]
     )

       partner = st.selectbox(
        "Partner",
        ["Yes", "No"]
     )

       dependents = st.selectbox(
        "Dependents",
        ["Yes", "No"]
     )

       tenure = st.number_input(
        "Tenure (Months)",
        min_value=0,
        max_value=72,
        value=12
     )

       phone_service = st.selectbox(
        "Phone Service",
        ["Yes", "No"]
     )

       multiple_lines = st.selectbox(
        "Multiple Lines",
        ["No", "Yes", "No phone service"]
     )

       internet_service = st.selectbox(
        "Internet Service",
        ["DSL", "Fiber optic", "No"]
     )

       online_security = st.selectbox(
        "Online Security",
        ["Yes", "No", "No internet service"]
     )

       online_backup = st.selectbox(
        "Online Backup",
        ["Yes", "No", "No internet service"]
     )

     

    with col2:
       
       device_protection = st.selectbox(
        "Device Protection",
        ["Yes", "No", "No internet service"]
     )

       tech_support = st.selectbox(
        "Tech Support",
        ["Yes", "No", "No internet service"]
     )

       streaming_tv = st.selectbox(
        "Streaming TV",
        ["Yes", "No", "No internet service"]
     )

       streaming_movies = st.selectbox(
        "Streaming Movies",
        ["Yes", "No", "No internet service"]
     )

       contract = st.selectbox(
        "Contract",
        ["Month-to-month", "One year", "Two year"]
     )

       paperless_billing = st.selectbox(
        "Paperless Billing",
        ["Yes", "No"]
     )

       payment_method = st.selectbox(
        "Payment Method",
        [
            "Electronic check",
            "Mailed check",
            "Bank transfer (automatic)",
            "Credit card (automatic)"
        ]
     )

       monthly_charges = st.number_input(
        "Monthly Charges",
        min_value=0.0,
        value=70.0
     )

       total_charges = st.number_input(
        "Total Charges",
        min_value=0.0,
        value=1000.0
     )

     
    
    predict = st.button("Predict Churn")


    if predict:

     input_data = pd.DataFrame({
        "gender": [gender],
        "SeniorCitizen": [senior_citizen],
        "Partner": [partner],
        "Dependents": [dependents],
        "tenure": [tenure],
        "PhoneService": [phone_service],
        "MultipleLines": [multiple_lines],
        "InternetService": [internet_service],
        "OnlineSecurity": [online_security],
        "OnlineBackup": [online_backup],
        "DeviceProtection": [device_protection],
        "TechSupport": [tech_support],
        "StreamingTV": [streaming_tv],
        "StreamingMovies": [streaming_movies],
        "Contract": [contract],
        "PaperlessBilling": [paperless_billing],
        "PaymentMethod": [payment_method],
        "MonthlyCharges": [monthly_charges],
        "TotalCharges": [total_charges]
    })

     prediction = pipeline.predict(input_data)

     probability = pipeline.predict_proba(input_data)

     churn_probability = probability[0][1] * 100

     if prediction[0] == 1:
        st.error("⚠️ Customer is likely to Churn")
     else:
        st.success("✅ Customer is not likely to Churn")

     
     st.metric(
        label="Churn Probability",
        value=f"{churn_probability:.2f}%"
)

     if churn_probability < 30:
        st.success("🟢 Risk Level: Low")

     elif churn_probability < 70:
        st.warning("🟡 Risk Level: Medium")

     else:
        st.error("🔴 Risk Level: High")



     st.subheader("Business Recommendation")


     if churn_probability < 30:

        st.success("""
        ✅ Customer has a low churn risk.

        Recommendation:
        - Continue regular engagement.
        - Maintain current service quality.
         """)

     elif churn_probability < 70:

        st.warning("""
     ⚠️ Customer has a medium churn risk.

         Recommendation:
         - Offer promotional discounts.
         - Send personalized offers.
         - Improve customer engagement.
        """)

     else:

        st.error("""
    
                 
       🚨 Customer has a high churn risk.

       Recommendation:
       - Offer a long-term contract.
       - Provide loyalty discounts.
       - Assign customer support for follow-up.
       """)
        
     st.subheader("Customer Summary")
     st.dataframe(input_data)
    



