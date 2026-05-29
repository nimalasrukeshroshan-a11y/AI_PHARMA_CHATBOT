# PharmAI Assistant 💊

PharmAI Assistant is a beginner-friendly AI-powered medical information assistant built using Streamlit, MongoDB, and Ollama AI.

The application allows users to create accounts with their medical profiles and receive personalized medicine guidance based on:

* Age
* Allergies
* Existing medical conditions
* Current medications

The project follows a clean modular architecture and uses secure authentication with hashed passwords.

---

# Features

✅ User Signup & Login Authentication
✅ Secure Password Hashing using bcrypt
✅ MongoDB Database Integration
✅ Personalized AI Drug Guidance
✅ Medication Interaction Warnings
✅ Allergy Risk Detection
✅ Query History Tracking
✅ Streamlit Professional UI
✅ Ollama Local AI Integration
✅ Modular Beginner-Friendly Python Code
✅ Environment Variable Security
✅ Responsive Dashboard Layout

---

# Tech Stack

* Python
* Streamlit
* MongoDB
* pymongo
* Ollama AI
* bcrypt
* python-dotenv

---

# Project Structure

```bash
pharmai-assistant/
│
├── app.py
├── main.py
├── requirements.txt
├── .env
├── .gitignore
├── README.md
│
├── database/
│   ├── mongodb.py
│   └── queries.py
│
├── auth/
│   ├── login.py
│   ├── signup.py
│   └── security.py
│
├── ai/
│   ├── ollama_client.py
│   └── prompt_builder.py
│
├── ui/
│   ├── sidebar.py
│   ├── history.py
│   └── styles.py
│
├── utils/
│   ├── session_manager.py
│   ├── validators.py
│   └── helpers.py
│
└── assets/
    └── logo.png
```

---

# MongoDB Setup

## Step 1 — Install MongoDB

Install MongoDB locally or use MongoDB Atlas.

MongoDB Atlas:
https://www.mongodb.com/atlas/database

---

## Step 2 — Create Database

Create a database named:

```bash
pharmai_db
```

Collections:

```bash
users
query_history
```

---

# Ollama Setup

## Step 1 — Install Ollama

Download Ollama from:

https://ollama.com/download

---

## Step 2 — Pull AI Model

Example:

```bash
ollama pull llama3
```

---

## Step 3 — Start Ollama

Run:

```bash
ollama run llama3
```

Make sure Ollama is running locally before starting the Streamlit app.

---

# Environment Variables

Create a `.env` file in the root folder.

Example:

```env
MONGODB_URI=your_mongodb_connection_string
```

No external API keys are required because Ollama runs locally.

---

# Installation Steps

## Step 1 — Clone Repository

```bash
git clone https://github.com/yourusername/pharmai-assistant.git
```

---

## Step 2 — Open Project

```bash
cd pharmai-assistant
```

---

## Step 3 — Install Requirements

```bash
pip install -r requirements.txt
```

---

# Run the Application

```bash
streamlit run app.py
```

---

# Main Functionalities

## Authentication System

Users can:

* Create accounts
* Login securely
* Store medical profiles

Passwords are securely hashed using bcrypt.

---

## Personalized AI Responses

The AI generates responses based on:

* User age
* Allergies
* Medical conditions
* Current medications

The assistant provides:

* Drug usage
* Dosage guidance
* Side effects
* Safety precautions
* Medication interaction alerts

---

## Query History

Users can view their previous medicine-related questions and AI responses.

The latest 10 queries are displayed on the dashboard.

---

# Security Features

✅ Password hashing using bcrypt
✅ Environment variables with dotenv
✅ Secure MongoDB queries
✅ Duplicate email prevention
✅ Input validation
✅ Session state protection
✅ No plaintext passwords
✅ Safe error handling

---

# requirements.txt

```txt
streamlit
pymongo
bcrypt
python-dotenv
ollama
pandas
```

---

# Future Improvements

* PDF medical reports
* Voice assistant
* Multi-language support
* Doctor appointment integration
* Medicine recommendation engine

---

# Disclaimer

PharmAI Assistant provides AI-generated medical information for educational purposes only.

This application does not replace professional medical advice, diagnosis, or treatment.

Always consult a licensed doctor or pharmacist before taking any medication.

