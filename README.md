# 🤖 AI Chatbot (FastAPI + Groq)

An AI-powered chatbot web application built using **FastAPI**, **LangChain**, and **Groq LLaMA 3.1**. This project provides fast and intelligent real-time responses through a simple and user-friendly web interface.

---

## 🚀 Features

- ⚡ Real-time chatbot responses
- 🧠 Powered by Groq LLaMA 3.1 (via LangChain)
- 🚀 FastAPI backend for high-performance APIs
- 🎨 Clean and responsive frontend (HTML, CSS, JavaScript)
- 🔗 Seamless API communication using Fetch

---

## 🛠️ Tech Stack

- **Backend:** FastAPI, Python  
- **AI Engine:** LangChain + Groq (LLaMA 3.1)  
- **Frontend:** HTML, CSS, JavaScript  
- **API Communication:** REST (JSON)

---

## 📂 Project Structure
llm_chatbot/
│
├── backend/
│ ├── app.py
│ └── init.py
│
├── front_end/
│ ├── index.html
│ ├── style.css
│ └── script.js
│
├── .env
├── .gitignore
└── README.md


---

---

## ⚙️ Setup & Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/razimk/LLM-chatbot.git
cd LLM-chatbot
2️⃣ Create Virtual Environment
python -m venv .venv

Activate it:

# Windows
.venv\Scripts\activate

# Mac/Linux
source .venv/bin/activate
3️⃣ Install Dependencies
pip install fastapi uvicorn langchain langchain-groq python-dotenv
4️⃣ Add Environment Variables

Create a .env file in the root directory:

GROQ_API_KEY=your_api_key_here

⚠️ Do not share your API key publicly

▶️ Running the Application
🔹 Start Backend Server
cd backend
uvicorn app:app --reload

Backend runs at:

http://127.0.0.1:8000
🔹 Start Frontend Server

Open a new terminal:

cd front_end
python -m http.server 5500
🌐 Open in Browser
http://127.0.0.1:5500
🧠 How It Works
User enters a message in the UI
Frontend sends a request to FastAPI backend
Backend processes input using Groq LLM
AI generates a response
Response is sent back and displayed instantly
🧪 API Testing

You can test the API using Swagger UI:

http://127.0.0.1:8000/docs
🎯 Use Cases
AI chatbot interface
Customer support assistant
Learning LLM integration
Base for advanced AI projects
🔮 Future Improvements
💬 Chat history & memory
🔐 User authentication
🎨 Enhanced UI/UX
☁️ Cloud deployment (Streamlit / Render)
📌 Notes
Ensure backend runs on port 8000
Always start frontend using a server (not file://)
Keep .env secure and private
⭐ Contributing

Feel free to fork this repository and improve it!

📜 License

This project is open-source and available under the MIT License.

🙌 Acknowledgements
FastAPI
LangChain
Groq LLM

## 📸 Chatbot UI

![Chatbot UI](Screenshot.png)