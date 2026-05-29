# PharmAI Assistant 💊

An **AI-powered personalized drug information assistant** built with Streamlit, Gorq API, and MongoDB.

Users create accounts with their medical profiles and receive **AI-generated medication guidance** customized to their health conditions, allergies, age, and current medications.

---

## ✨ Features

- **🔐 Secure User Authentication**
  - Account creation with medical profile
  - Password hashing with bcrypt
  - Secure login/logout

- **🏥 Medical Profile Management**
  - Track age, allergies, medical conditions, and current medications
  - Personalized recommendations based on medical history

- **🤖 AI-Powered Medication Guidance**
  - Ask questions about medications
  - Get personalized responses using Gorq API
  - Automatic drug interaction detection
  - Allergy risk warnings

- **📋 Query History**
  - View last 10 queries
  - Access previous responses
  - Timestamp tracking

- **💾 Secure Data Storage**
  - MongoDB Atlas integration
  - Encrypted passwords
  - Secure session management

---

## 📁 Project Structure

```
pharmai-assistant/
│
├── app.py                     # Streamlit frontend entry point
├── main.py                    # Backend logic controller
├── requirements.txt           # Python dependencies
├── .env                       # Environment variables (KEEP SECRET!)
├── .gitignore                 # Git ignore file
├── README.md                  # This file
│
├── database/
│   ├── mongodb.py             # MongoDB connection setup
│   └── queries.py             # Database operations (CRUD)
│
├── auth/
│   ├── login.py               # Login logic
│   ├── signup.py              # Signup and registration
│   └── security.py            # Password hashing & verification
│
├── ai/
│   ├── gorq_client.py         # Gorq API configuration
│   └── prompt_builder.py      # Dynamic personalized prompts
│
├── ui/
│   ├── sidebar.py             # Sidebar UI component
│   ├── history.py             # Query history display
│   └── styles.py              # Custom CSS styling
│
├── utils/
│   ├── session_manager.py     # Streamlit session management
│   ├── validators.py          # Input validation
│   └── helpers.py             # Helper utilities
│
└── assets/
    └── (placeholder for images/assets)
```

---

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- MongoDB Atlas account
- Gorq API key

### Installation Steps

#### 1. Clone or Extract the Project

```bash
cd pharmai-assistant
```

#### 2. Create Virtual Environment (Recommended)

```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

#### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

#### 4. Configure Environment Variables

Edit the `.env` file and add your credentials:

```env
MONGODB_URI=your_mongodb_connection_string_here
GORQ_API_KEY=your_gorq_api_key_here
```

**⚠️ IMPORTANT:** Never commit `.env` file to version control!

#### 5. Run the Application

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

---

## 🔧 Configuration

### MongoDB Setup

1. **Create MongoDB Atlas Account**
   - Go to [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)
   - Create a free cluster
   - Create a database user with appropriate credentials

2. **Get Connection String**
   - In Atlas, click "Connect"
   - Select "Drivers"
   - Copy the Python connection string
   - Replace password and database name

3. **Add to .env**
   ```
   MONGODB_URI=mongodb+srv://username:password@cluster.mongodb.net/pharmai_assistant?retryWrites=true&w=majority
   ```

### Gorq API Setup

1. **Get API Key**
   - Visit your Gorq dashboard or API key manager
   - Create a new API key
   - Copy the key

2. **Add to .env**
   ```
   GORQ_API_KEY=your_api_key_here
   ```

---

## 📊 Database Design

### users collection

```json
{
  "_id": "ObjectId",
  "name": "John Doe",
  "email": "john@example.com",
  "password": "bcrypt_hashed_password",
  "age": 30,
  "known_allergies": ["penicillin", "aspirin"],
  "existing_conditions": ["diabetes", "hypertension"],
  "current_medications": ["metformin", "lisinopril"],
  "created_at": "2024-01-15T10:30:00Z"
}
```

### query_history collection

```json
{
  "_id": "ObjectId",
  "user_id": "ObjectId",
  "query": "What are the side effects of aspirin?",
  "response": "AI-generated response...",
  "timestamp": "2024-01-15T10:35:00Z"
}
```

---

## 🔒 Security Features

✅ **Password Hashing** - bcrypt with 12 rounds
✅ **Environment Variables** - Sensitive data in .env
✅ **Input Validation** - All user inputs validated
✅ **Email Uniqueness** - Duplicate email prevention
✅ **Session Management** - Secure Streamlit sessions
✅ **Error Handling** - No stack traces exposed to users
✅ **MongoDB Indexing** - Optimized queries with indexes

---

## 💊 How It Works

### 1. User Registration
- User fills out signup form with medical profile
- Password is hashed with bcrypt
- Profile saved to MongoDB

### 2. User Login
- Email and password validated
- Password verified against hash
- Session state updated
- User redirected to dashboard

### 3. Medication Query
- User asks a medication-related question
- AI builds personalized prompt using medical profile
- Gorq API generates response with:
  - Drug information
  - Side effects
  - Dosage information
  - **Interaction detection** with current medications
  - **Allergy warnings** based on known allergies
- Response saved to query history
- User displays response with disclaimer

### 4. Query History
- Last 10 queries displayed in expandable sections
- Sorted by most recent first
- Includes timestamps and full responses

---

## 🎯 Usage Examples

### Example 1: Medication Query
```
User: "I have diabetes and take metformin. Can I take ibuprofen for headaches?"

AI Response includes:
- Information about ibuprofen
- Interaction check with metformin
- Dosage recommendations for diabetic patients
- Safety precautions
- Medical disclaimer
```

### Example 2: Allergy Check
```
User: "Is it safe for me to take amoxicillin?"
Medical Profile: Known allergy to penicillin

AI Response includes:
- 🚨 DANGER warning: Amoxicillin is a penicillin-based antibiotic
- Recommendation to avoid
- Alternative antibiotics to discuss with doctor
```

---

## 📋 API Response Format

The AI generates responses with:

```
### Drug Information
- What it is and uses
- How it works

### Dosage
- Typical dosage ranges
- Frequency of use

### Side Effects
- Common side effects
- Serious side effects to watch

### Safety Precautions
- Contraindications
- Special populations (elderly, pregnant, etc.)

### [INTERACTION WARNINGS if applicable]
⚠️ WARNING: Possible interaction with your current medications

### [ALLERGY WARNINGS if applicable]
🚨 DANGER: This medication may trigger your allergies

### Personalized Notes
Based on your age and medical profile...

---
**Disclaimer:** This information is AI-generated and does not replace professional medical advice...
```

---

## 🐛 Troubleshooting

### Issue: "Failed to connect to MongoDB"
- ✅ Check MongoDB URI in .env file
- ✅ Verify database credentials
- ✅ Ensure IP address is whitelisted in MongoDB Atlas
- ✅ Test connection: `python -c "from database.mongodb import connect_to_mongodb; connect_to_mongodb()"`

### Issue: "Gorq API error"
- ✅ Check API key in .env file
- ✅ Verify API key is valid and not expired
- ✅ Ensure Gorq API access is enabled for your account
- ✅ Check API usage quota

### Issue: "Email already exists"
- ✅ Use a different email address
- ✅ Or login with existing email if you already have an account

### Issue: "Invalid password format"
- ✅ Password must be at least 6 characters
- ✅ No special character requirements, keep it simple

---

## 📚 Technologies Used

| Technology | Purpose |
|-----------|---------|
| **Streamlit** | Web UI framework |
| **Python** | Backend programming |
| **MongoDB** | NoSQL database |
| **Gorq API** | AI/ML responses |
| **bcrypt** | Password hashing |
| **python-dotenv** | Environment variables |

---

## 🔐 Security Best Practices

1. **Never commit .env file** - Add to .gitignore (already done)
2. **Use strong passwords** - Minimum 6 characters recommended
3. **Keep API keys secret** - Don't share or expose in code
4. **Use HTTPS** - Deploy with HTTPS in production
5. **Validate all inputs** - Already implemented in the app
6. **Regular backups** - Backup MongoDB regularly
7. **Monitor logs** - Check for suspicious activity

---

## 🚀 Deployment

### Deploy to Streamlit Cloud (Recommended for Beginners)

1. Push code to GitHub
2. Go to [Streamlit Cloud](https://share.streamlit.io/)
3. Connect GitHub repository
4. Set environment variables in Streamlit Cloud settings
5. Deploy!

### Deploy to Other Platforms

- **AWS**: Use EC2 + Streamlit
- **Heroku**: Use Procfile + Streamlit
- **Docker**: Containerize with Docker image
- **Google Cloud**: Use Cloud Run

---

## 📝 Example .env File

```env
# MongoDB Connection String
MONGODB_URI=mongodb+srv://username:password@cluster0.asgewcv.mongodb.net/pharmai_assistant?retryWrites=true&w=majority

# Gorq API Key
GORQ_API_KEY=your_gorq_api_key_here
```

---

## 🎓 Learning Resources

- [Streamlit Documentation](https://docs.streamlit.io/)
- [MongoDB Python Guide](https://docs.mongodb.com/languages/python/)
- [Gorq API Docs](https://gorq.ai/)
- [bcrypt Python](https://github.com/pyca/bcrypt)

---

## 🤝 Contributing

This is a complete project. For improvements or issues:

1. Review code quality
2. Test all features
3. Document changes
4. Update README if needed

---

## 📄 License

This project is provided as-is for educational and commercial use.

---

## ⚠️ Disclaimer

**PharmAI Assistant is an AI-powered information tool, NOT a replacement for professional medical advice.**

- Always consult a licensed healthcare provider before taking medications
- Do not use this app for medical emergencies
- Verify all information with qualified physicians
- This app is for informational purposes only

---

## 🆘 Support

For issues or questions:

1. Check the Troubleshooting section
2. Review error messages in terminal
3. Check MongoDB/API credentials
4. Consult documentation links above

---

## 🎉 You're All Set!

Start using PharmAI Assistant:

```bash
streamlit run app.py
```

**Enjoy personalized medication guidance! 💊**

---

*Last Updated: January 2024*
*Version: 1.0.0*
