import streamlit as st 
from datetime import datetime



st.title("The Recipe Hub")

current_date = datetime.now().strftime("%B %d, %Y")

st.header("Frank Gadri")
st.subheader(f"Date Created: {current_date}")