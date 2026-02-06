import streamlit as st

# Streamlit ui
st.title("Power Calculator")
st.write("Enter a number to calculkate its squarem cube and fifth power.")

# Get your input
n = st.number_input("Enter an integer", value=1, step=1)

# Calculate results
square = n ** 2
cube = n**3
fifth_power = n**5

# Display results
st.write("The square of {n} is: {square}")
st.write(f"The cube of {n} is: {cube}")
st.write(f"The fifth power of {n} is: {fifth_power}")

