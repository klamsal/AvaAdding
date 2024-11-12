import streamlit as st

# Streamlit app for a simple adding app for kids
st.title("Fun Adding App for Kids!")
st.markdown("<h2 style='color:purple;'>Let's add two numbers together!</h2>", unsafe_allow_html=True)

# Ask for the first number
first_number = st.number_input("Enter the first number:", min_value=0, step=1, key='first_number')

# Ask for the second number
second_number = st.number_input("Enter the second number:", min_value=0, step=1, key='second_number')

# Calculate the sum
if st.button("Add Them Up!"):
    result = first_number + second_number
    st.markdown(f"<h3 style='color:orange;'>The sum is: {result}</h3>", unsafe_allow_html=True)
