import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

from inference.predict_freight import predict_freight_cost
from inference.predict_invoice import predict_invoice_flag

# Page configuration
st.set_page_config(
    page_title="Vendor Invoice Intelligence Portal",
    page_icon="🫶",
    layout="wide"
)

# Header Section
st.markdown("""
    # Vendor Invoice Intelligence Portal
    ### AI-Driven Freight Cost Predictions and Invoice Risk Flagging
    
    This Internal analytics portal leverages machine learning to 
    - ** Forecast freight cost accurately **
    - ** Detect risky or abnormal vendor invoices **
    - ** Reduce financial leakage and manual workloads **             
""")

st.divider()

# Sidebar
st.sidebar.title("Model Selection")
selected_model = st.sidebar.radio(
    "Choose Prediction Module",
    [
        "Freight Cost Prediction",
        "Invoice Manual Approval Flag"
    ]
)

st.sidebar.markdown("""
    ---
    ** Busines Impact **
    - Improved cost forecasting
    - Reduced invoice fraud and anomalies
    - Faster finance operations                    
""")

# Freight Cost Prediction
if selected_model == "Freight Cost Prediction":
    st.subheader("Freight Cost Prediction")
                 
    st.markdown(
        """
        **Objective:**
        Predict freight cost for a vendor invoice **Quantity** and **Invoice Dollars**
        to support budgeting, forecasting, and vendor negotiations,
        """
    )
    
    with st.form("freight_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            quantity = st.number_input(
                "Quantity",
                min_value=1,
                value=1200
            )
        
        with col2:
            dollars = st.number_input(
                "Invoice Dollars",
                min_value=1.0,
                value=18500.0
            )
            
        submit_freight = st.form_submit_button("Predict freight cost")
        
    if submit_freight:
        input_data = {
            "Quantity": {quantity},
            "Dollars": {dollars}
        }
        
        prediction = predict_freight_cost(input_data)["Predicted_Freight"]
        
        st.success("Prediction completed successfully.")
        
        st.metric(
            label="Estimated Freight Cost",
            value=f"${prediction[0]:.2f}"
        )
        
# Invoice flag prediction
