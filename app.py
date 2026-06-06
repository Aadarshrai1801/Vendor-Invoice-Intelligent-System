import streamlit as st
from inference.predict_freight import predict_freight_cost
from inference.predict_invoice import predict_invoice_flag

# ---------------------------------------------------
# Page Configuration
# ---------------------------------------------------
st.set_page_config(
    page_title="Vendor Invoice Intelligence Portal",
    page_icon="📊",
    layout="wide"
)

# ---------------------------------------------------
# Custom CSS
# ---------------------------------------------------
st.markdown("""
<style>

.main {
    background-color: #f6f8fc;
}

.hero {
    background: linear-gradient(135deg,#1f4e79,#2563eb);
    padding: 2rem;
    border-radius: 20px;
    color: white;
    margin-bottom: 1.5rem;
}

.hero h1{
    margin-bottom:0;
}

.hero p{
    font-size:18px;
    opacity:0.95;
}

.metric-card {
    background:white;
    padding:20px;
    border-radius:15px;
    box-shadow:0px 3px 15px rgba(0,0,0,0.08);
}

.stButton > button {
    width:100%;
    border-radius:10px;
    height:50px;
    font-weight:bold;
    font-size:16px;
}

section[data-testid="stSidebar"] {
    background-color:#1e293b;
}

section[data-testid="stSidebar"] * {
    color:white !important;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# Header
# ---------------------------------------------------
st.markdown("""
<div class="hero">
    <h1>📊 Vendor Invoice Intelligence Portal</h1>
    <p>
        AI-powered freight forecasting and invoice risk detection platform
        for finance and procurement teams.
    </p>
</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# Sidebar
# ---------------------------------------------------
st.sidebar.title("⚙️ Prediction Modules")

selected_model = st.sidebar.radio(
    "Select Module",
    [
        "Freight Cost Prediction",
        "Invoice Risk Assessment"
    ]
)

st.sidebar.markdown("---")

st.sidebar.markdown("""
### 🚀 Business Benefits

✅ Accurate freight forecasting

✅ Reduced invoice anomalies

✅ Faster approval workflows

✅ Better vendor negotiations

✅ Improved operational efficiency
""")

# ---------------------------------------------------
# Dashboard Stats
# ---------------------------------------------------
c1, c2, c3 = st.columns(3)

with c1:
    st.metric("Models Available", "2")

with c2:
    st.metric("Prediction Type", "ML")

with c3:
    st.metric("System Status", "Online")

st.divider()

# ===================================================
# Freight Prediction
# ===================================================
if selected_model == "Freight Cost Prediction":

    st.subheader("🚚 Freight Cost Prediction")

    st.info(
        "Predict freight expenses from invoice dollar amount to support budgeting and forecasting."
    )

    with st.container(border=True):

        with st.form("freight_form"):

            dollars = st.number_input(
                "Invoice Dollars ($)",
                min_value=1.0,
                value=18500.0,
                step=100.0
            )

            submit_freight = st.form_submit_button(
                "🔮 Predict Freight Cost"
            )

    if submit_freight:

        input_data = {
            "Dollars": [dollars]
        }

        prediction = predict_freight_cost(
            input_data
        )["Predicted_Freight"].iloc[0]

        st.success("Prediction generated successfully.")

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Predicted Freight Cost",
                f"${prediction:,.2f}"
            )

        with col2:
            ratio = prediction / dollars * 100

            st.metric(
                "Freight %",
                f"{ratio:.2f}%"
            )

# ===================================================
# Invoice Risk Assessment
# ===================================================
else:

    st.subheader("🛡️ Invoice Risk Assessment")

    st.info(
        "Detect invoices that may require manual approval due to unusual patterns."
    )

    with st.container(border=True):

        with st.form("invoice_flag_form"):

            col1, col2, col3 = st.columns(3)

            with col1:

                invoice_quantity = st.number_input(
                    "Invoice Quantity",
                    min_value=1,
                    value=50
                )

                freight = st.number_input(
                    "Freight Cost",
                    min_value=0.0,
                    value=1.73
                )

            with col2:

                invoice_dollars = st.number_input(
                    "Invoice Dollars",
                    min_value=1.0,
                    value=352.95
                )

                total_item_quantity = st.number_input(
                    "Total Item Quantity",
                    min_value=1,
                    value=162
                )

            with col3:

                total_item_dollars = st.number_input(
                    "Total Item Dollars",
                    min_value=1.0,
                    value=2476.0
                )

            submit_flag = st.form_submit_button(
                "🔍 Evaluate Invoice"
            )

    if submit_flag:

        input_data = {
            "invoice_quantity": [invoice_quantity],
            "invoice_dollars": [invoice_dollars],
            "Freight": [freight],
            "total_item_quantity": [total_item_quantity],
            "total_item_dollars": [total_item_dollars]
        }

        prediction = predict_invoice_flag(
            input_data
        )["Predicted_Flag"].iloc[0]

        if bool(prediction):

            st.error(
                "🚨 High Risk Invoice Detected\n\nManual approval is recommended."
            )

        else:

            st.success(
                "✅ Low Risk Invoice\n\nSafe for automated approval."
            )

# ---------------------------------------------------
# Footer
# ---------------------------------------------------
st.divider()

st.caption(
    "Vendor Invoice Intelligence Portal | Machine Learning Powered Finance Analytics"
)