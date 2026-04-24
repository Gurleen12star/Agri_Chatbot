# 🌾 AgriChatbot – Smart Farming Assistant  
*(Tasks 1 → 4 Integrated Project)*

> AI-powered chatbot for farmers with multilingual support and crop image analysis.

---

## ✨ Features

- 💬 Smart agriculture chatbot  
- 🔐 User login & registration  
- 👨‍💼 Admin dashboard  
- 🌐 Supports English, Hindi, Punjabi  
- 📷 AI crop image analysis  
- 🤖 OpenAI-powered responses  

---

## 🧩 Modules

### 🟢 Task 1 – Chatbot
Basic Flask chatbot for queries  

### 🔵 Task 2 – Auth + DB
Login, register, database + OpenAI  

### 🟡 Task 3 – Admin + Translation
Admin panel + multilingual chat  

### 🔴 Task 4 – Image Analysis
Upload images → AI crop insights  

---

## 🛠️ Tech Stack

**Backend:** Python, Flask  
**Frontend:** HTML, CSS, JavaScript  
**Database:** SQLite / MySQL  
**AI:** OpenAI API  
**Tools:** GitHub, VS Code  

---

## 🖼 Screenshots

<img src="https://github.com/user-attachments/assets/104e31dd-ea73-47b0-959c-411ce10fb48e" width="100%" />
<img src="https://github.com/user-attachments/assets/3b6aab74-2416-4525-b673-fd75eb5dec7e" width="100%" />
<img src="https://github.com/user-attachments/assets/98ca8f5e-8611-4be1-b9e4-06948a8e5c33" width="100%" />
<img src="https://github.com/user-attachments/assets/f43d735a-0e6d-4cde-9d71-7fd472dbe7e7" width="100%" />
<img src="https://github.com/user-attachments/assets/8e6c1c1e-ae1a-4e11-8a9c-055861c6edc5" width="100%" />

---

## ⚙️ How It Works

1. User logs in  
2. Sends query or uploads image  
3. Flask backend processes request  
4. OpenAI generates response  
5. Response translated (if needed)  
6. Output shown to user  

---

## 🔄 Workflow

```mermaid
flowchart TD
    A[User Input] --> B[Flask Backend]
    B --> C{Type}

    C -->|Text| D[OpenAI Chat]
    C -->|Image| E[OpenAI Vision]

    D --> F[Response]
    E --> F

    F --> G[Translate]
    G --> H[Display]
graph LR
    User --> Frontend
    Frontend --> Flask
    Flask --> Database
    Flask --> OpenAI
    OpenAI --> Flask
    Flask --> Frontend

##⚙️ Run Locally
git clone https://github.com/yourusername/agrichatbot.git

cd task4   # or task1/task2/task3

pip install -r requirements.txt
python app.py
👉 Runs on: http://127.0.0.1:5000

🚀 Future Work
📱 Mobile app
🌱 Better crop detection
🌍 More languages
📊 Analytics dashboard
👨‍💻 Author
Your Name
📜 License

MIT License
