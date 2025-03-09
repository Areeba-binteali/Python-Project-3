import streamlit as st
import re
import random
import string

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
        return 0  # Weakest score

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


     # Generate dynamic width for progress bar
    progress_width = (score / 5) * 100  # Convert score (0-5) to percentage (0-100)

    # HTML for progress bar with gradient colors
    if (progress_width == 20):
        progress_bar_html = f"""
        <div style="width: 100%; background-color: white; border-radius: 10px;">
            <div style="
                width: {progress_width}%;
                height: 10px;
                border-radius: 10px;
                background: linear-gradient(to right, red, red);
                "></div>
        </div>
        """
        
    if (progress_width == 40):
        progress_bar_html = f"""
        <div style="width: 100%; background-color: white; border-radius: 10px;">
            <div style="
                width: {progress_width}%;
                height: 10px;
                border-radius: 10px;
                background: linear-gradient(to right, red, orange);
                "></div>
        </div>
        """

    if (progress_width == 60):
        progress_bar_html = f"""
        <div style="width: 100%; background-color: white; border-radius: 10px;">
            <div style="
                width: {progress_width}%;
                height: 10px;
                border-radius: 10px;
                background: linear-gradient(to right, red, #eb5834, orange);
                "></div>
        </div>
        """

    if (progress_width == 80):
        progress_bar_html = f"""
        <div style="width: 100%; background-color: white; border-radius: 10px;">
            <div style="
                width: {progress_width}%;
                height: 10px;
                border-radius: 10px;
                background: linear-gradient(to right, red, #eb5834, orange, yellow);
                "></div>
        </div>
        """

    if (progress_width == 100):
        progress_bar_html = f"""
        <div style="width: 100%; background-color: white; border-radius: 10px;">
            <div style="
                width: {progress_width}%;
                height: 10px;
                border-radius: 10px;
                background: linear-gradient(to right, red, #eb5834, orange, yellow, green);
                "></div>
        </div>
        """

    if score == 5:
        st.markdown(progress_bar_html, unsafe_allow_html=True)
        st.write("✅ Strong Password!")
        st.balloons()
    elif score >= 3: 
        suggest_strong_password()
        st.markdown(progress_bar_html, unsafe_allow_html=True)
        st.write("⚠️ Moderate Password - Consider adding more security features.")
    else:
        suggest_strong_password()
        st.markdown(progress_bar_html, unsafe_allow_html=True)
        st.write("❌ Weak Password - Improve it using the suggestions below.")

    return score  # Return score to update the progress bar

# Function to suggest a strong password
def suggest_strong_password():
    password = ''.join(random.choices(string.ascii_letters + string.digits + "!@#$%^&*", k=12))
    st.write("💡 Suggested Strong Password:")
    st.code(password)

# Streamlit UI
st.title("🔐 Password Strength Checker")

# Password Input Field
password = st.text_input("Enter your password:", key="password")

# Display the entered password
st.code(password)

# Check password strength
if password:
    strength = check_password_strength(password)

   