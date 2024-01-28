import streamlit as st
import pandas as pd
from joblib import load


model = load(r"C:\Users\ST\Downloads\my_telco_trained_model.joblib")
st.title("Telecom Customer churun prediction App")
st.header("Enter Customer Information")
tenure = st.number_input("Tenure in moths", min_value= 0, max_value=100)

internet_service = st.selectbox("Internet Service", ("DSL", "Fiber_Optic", "No"))

monthly_charges = st.number_input("Monthly Charges", min_value= 0, max_value=1000)

contract = st.selectbox("Contracts", ("Month", "Year1", "Year2"))
total_Charges = st.number_input("Total Charges", min_value= 0, max_value=10000000)

if internet_service=="DSL":
    internet_service_arr = [1,0,0]
    
elif internet_service=="Fiber_Optic":
    internet_service_arr = [0,1,0]
    
else:
    internet_service_arr = [1,0,0]

if contract == "Month":
    contract_arr = [1,0,0]
elif contract == "Year1":
    contract_arr = [0,1,0]
else:
    contract_arr = [0,0,1]
input_arr= []
input_arr.append(tenure)

input_arr.append(monthly_charges)

input_arr.append(total_Charges)

input_arr+= contract_arr
input_arr += internet_service_arr
print(input_arr)


prediction  = model.predict([input_arr])
print(prediction[0])
st.header("Prediction Header: ")
if prediction[0] == 0:
    st.success("this Customer is likely to stay")
else:
    st.success("this Customer is going to leave")


