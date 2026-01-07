AI-Powered Phishing Detector 🛡️
An integrated machine learning solution designed to identify phishing attempts across two primary vectors: Malicious URLs and Scam Emails. This project uses Natural Language Processing (NLP) and supervised learning to classify content as "Safe" or "Phishing."

🚀 Features
Email Classifier: Detects fraudulent patterns in email body text using TF-IDF vectorization.

URL Analyzer: Evaluates website links based on structural features.

Dual-Model Architecture: Uses pre-trained .pkl models for fast, real-time inference.

Jupyter Notebook: Includes system.ipynb for the full data analysis and training pipeline.

📂 Project Structure
Plaintext

├── datasets/           # Training data (CSV files)
├── models/             # Saved model weights (.pkl)
├── notebooks/          # Training and EDA scripts (system.ipynb)
├── app.py              # Main application entry point
└── requirements.txt    # Project dependencies
🛠️ Installation & Setup
Clone the repository:

Bash

git clone https://github.com/your-username/your-repo-name.git
cd AI-Powered-Phishing-Detector
Create a virtual environment (Recommended):

Bash

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies:

Bash

pip install -r requirements.txt
📊 How it Works
Data Preprocessing: The system cleans text by removing stop words and special characters.

Vectorization: Emails are converted into numerical data using a Vectorizer.

Prediction: The models (email_model.pkl and url_model.pkl) output a probability score.

Result: The application returns a "Phishing" or "Legitimate" label.

🤖 Technologies Used
Python (Core Logic)

Scikit-Learn (Machine Learning)

Pandas/NumPy (Data Manipulation)

NLTK (Natural Language Processing)
