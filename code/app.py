import streamlit as st
import joblib
import numpy as np

# Load models and vectorizers
url_model = joblib.load("url_model.pkl")
url_scaler = joblib.load("url_scaler.pkl")
email_model = joblib.load("email_model.pkl")
email_vectorizer = joblib.load("email_vectorizer.pkl")

# Feature extraction function
def extract_full_url_features(url):
    return np.array([
        len(url), url.count('.'), url.count('/'), url.count('-'), url.count('='),
        url.count('?'), int('https' in url), int('http' in url),
        int('login' in url.lower()), int('secure' in url.lower()),
        int('@' in url), int('//' in url),
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0  # Fill with zeros for 32 features
    ]).reshape(1, -1)

# Unified phishing detection
def detect_phishing(input_type, content):
    if input_type == 'url':
        features = extract_full_url_features(content)
        features_scaled = url_scaler.transform(features)
        pred = url_model.predict(features_scaled)[0]
        return "🔒 Legitimate URL" if pred == 0 else "⚠️ Phishing URL"

    elif input_type == 'email':
        vectorized = email_vectorizer.transform([content])
        pred = email_model.predict(vectorized)[0]
        return "📧 Legitimate Email" if pred == 0 else "🚨 Spam/Phishing Email"

    return "Invalid input type."

# Streamlit UI
st.title("🔐 Phishing Detection System")
option = st.selectbox("Choose Input Type", ["URL", "Email"])

if option == "URL":
    url_input = st.text_input("Enter the URL:")
    if st.button("Check URL"):
        if url_input:
            st.success(detect_phishing("url", url_input))
        else:
            st.warning("Please enter a URL.")

elif option == "Email":
    email_input = st.text_area("Paste the email content:")
    if st.button("Check Email"):
        if email_input:
            st.success(detect_phishing("email", email_input))
        else:
            st.warning("Please paste some email content.")
st.markdown("""
---
📌 **Project created by Muhammad Ahmed Javed**
""")