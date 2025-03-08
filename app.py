import streamlit as st
import re
import random
import string
import pyperclip

# List of common passwords
common_passwords = [
    "password123", "123456", "123456789", "qwerty", "abc123", "letmein",
    "welcome", "password", "12345", "1234", "iloveyou", "admin", "password1",
    "sunshine", "qwerty123", "monkey", "123123", "welcome123", "1q2w3e4r",
    "123qwe", "1qaz2wsx", "qazwsx", "trustno1"
]

# Function to check password strength
def check_password_strength(password):
    if password.lower() in common_passwords:
        st.write("❌ This password is too common and insecure. Please choose a stronger one.")
        suggest_strong_password()
        return

    score = 0
    if len(password) >= 8:
        score += 1
    else:
        st.write("❌ Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        st.write("❌ Include at least 1 uppercase letter.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        st.write("❌ Include at least 1 lowercase letter.")

    if re.search(r"\d", password):
        score += 1
    else:
        st.write("❌ Add at least one number (0-9).")

    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        st.write("❌ Include at least one special character (!@#$%^&*).")

    if score == 5:
        st.write("✅ Strong Password!")
    elif score >= 3:
        st.write("⚠️ Moderate Password - Consider adding more security features.")
        suggest_strong_password()
    else:
        st.write("❌ Weak Password - Improve it using the suggestions above.")
        suggest_strong_password()

# Function to suggest a strong password
def suggest_strong_password():
    password = ''.join(random.choices(string.ascii_letters + string.digits + "!@#$%^&*", k=12))
    st.write(f"💡 Suggested Strong Password: {password}")

# Streamlit UI
st.title("🔐 Password Strength Checker")

# Initialize session state for button control
if "button_disabled" not in st.session_state:
    st.session_state.button_disabled = False


# Password Input Field
password = st.text_input("Enter your password:", key="password", on_change=lambda: setattr(st.session_state, "button_disabled", False))


# Check password strength when input is given
if password:
    check_password_strength(password)
