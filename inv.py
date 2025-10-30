import pip

import streamlit as st
import math

# ---- Page setup ----
st.set_page_config(page_title="Investment Advice Calculator", page_icon="💰", layout="centered")

st.title("💰 Investment Advice Calculator")
st.write("Get personalized investment insights based on your income, expenses, goals, and risk tolerance.")

# ---- User Inputs ----
st.header("Enter Your Financial Details")

income = st.number_input("Monthly Income (₹)", min_value=0.0, step=1000.0)
expenses = st.number_input("Monthly Expenses (₹)", min_value=0.0, step=1000.0)
age = st.slider("Age", 18, 70, 25)
savings = st.number_input("Current Savings (₹)", min_value=0.0, step=1000.0)
risk = st.radio("Risk Tolerance", ["Low", "Medium", "High"])
goal = st.selectbox("Investment Goal", ["Short-term", "Long-term", "Retirement"])

# ---- Calculate investable amount ----
if income > 0 and expenses > 0:
    investable = income - expenses
    if investable <= 0:
        st.warning("⚠️ You don’t have surplus income to invest. Try reducing expenses.")
    else:
        st.success(f"You can invest approximately ₹{investable:,.2f} per month.")
else:
    investable = 0

# ---- Portfolio Allocation ----
if risk == "Low":
    allocation = {"Debt Funds": 70, "Equity": 20, "Gold": 10}
    expected_return = 6
elif risk == "Medium":
    allocation = {"Debt Funds": 40, "Equity": 50, "Gold": 10}
    expected_return = 9
else:
    allocation = {"Debt Funds": 20, "Equity": 70, "Gold": 10}
    expected_return = 12

# ---- Future Value Calculation ----
years = st.slider("Investment Duration (Years)", 1, 30, 10)

if investable > 0:
    # Compound interest formula for SIP
    monthly_rate = expected_return / 100 / 12
    future_value = investable * (((1 + monthly_rate) ** (12 * years) - 1) / monthly_rate)

    st.subheader("📊 Suggested Portfolio Allocation")
    st.write(f"**Expected Annual Return:** {expected_return}%")

    st.bar_chart(allocation)

    st.subheader("📈 Future Investment Projection")
    st.write(f"Estimated Value after {years} years: **₹{future_value:,.2f}**")

    # Extra insights
    if goal == "Retirement":
        st.info("🧓 Consider adding NPS or long-term index funds to your plan.")
    elif goal == "Short-term":
        st.info("💼 Use low-risk debt or hybrid funds to protect capital.")
    else:
        st.info("🚀 Focus on diversified equity mutual funds for higher growth.")

st.markdown("---")
st.caption("💡 *Tip: Rebalance your portfolio every year to match your risk profile.*")
