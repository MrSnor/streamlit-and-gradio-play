import streamlit as st
import random
import string


def generate_password(length):
    alphanumeric = string.ascii_letters + string.digits
    password = ''.join(random.choice(alphanumeric) for i in range(length))
    return password


st.title("Alphanumeric Password Generator")
n_passwords = st.slider("Enter the number of passwords to generate:", 1, 25)
length = st.slider("Select password length:", 6, 20)

if st.button("Generate Passwords"):
    passwords = [generate_password(length) for _ in range(n_passwords)]
    st.write("Generated Passwords:")
    for i, password in enumerate(passwords):
        st.write(f"Password {i+1}: {password}")
