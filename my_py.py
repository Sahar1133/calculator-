# -*- coding: utf-8 -*-
"""my.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1JCt8AsD-yYjwutbrjZzX5JLqHN4HCMAT
"""

import logging
import streamlit as st

# Suppress specific warnings
logging.getLogger("streamlit").setLevel(logging.ERROR)

# Define the main function for the calculator
def calculator():
    st.title('Simple Streamlit Calculator')

    # Input fields for two numbers
    num1 = st.number_input('Enter first number', value=0)
    num2 = st.number_input('Enter second number', value=0)

    # Dropdown menu to select the operation
    operation = st.selectbox('Select operation', ('Add', 'Subtract', 'Multiply', 'Divide'))

    # Perform the selected operation
    if operation == 'Add':
        result = num1 + num2
    elif operation == 'Subtract':
        result = num1 - num2
    elif operation == 'Multiply':
        result = num1 * num2
    elif operation == 'Divide':
        if num2 != 0:
            result = num1 / num2
        else:
            result = 'Cannot divide by zero'

    # Display the result
    st.write(f'Result: {result}')

# Run the calculator
if __name__ == "__main__":
    calculator()