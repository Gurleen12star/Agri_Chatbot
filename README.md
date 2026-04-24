# 🌾 AgriChatbot – Smart Farming Assistant  
- AgriChatbot is an integrated AI + IoT smart agriculture system designed to assist farmers in making informed, real-time decisions. The project combines a web-based intelligent chatbot with a hardware-driven agribot ecosystem to address key challenges in modern farming such as irrigation management, crop health monitoring, and resource optimization.

On the software side, the system features an AI-powered chatbot built using Flask and OpenAI APIs. It allows users to ask agriculture-related questions, receive intelligent responses, and interact in multiple languages including English, Hindi, and Punjabi. The chatbot also supports image-based analysis, where farmers can upload crop images and receive insights about possible diseases or conditions using computer vision.

On the hardware side, the agribot integrates various sensors such as soil moisture and rain detection to automate farming processes. Based on real-time environmental data, the system can trigger irrigation, manage pesticide spraying, and support rainwater harvesting. These actions help conserve water, reduce manual effort, and improve crop productivity.

The entire system is connected through an IoT cloud platform, enabling remote monitoring and control. Sensor data is continuously uploaded to the cloud, allowing farmers to track field conditions through a dashboard or interface and make better decisions from anywhere.

By combining AI intelligence with IoT automation, this project demonstrates a scalable and practical approach to smart farming, aiming to improve efficiency, sustainability, and accessibility for modern agriculture.

> AI-powered chatbot for farmers with multilingual support and crop image analysis.

---

## ✨ Features

- 💬 Smart agriculture chatbot with voice support  
- 🔐 User login & registration  
- 👨‍💼 Admin dashboard with Knowledge Base
- 🌐 Supports English, Hindi, Punjabi plus 32 Regional languages   
- 📷 AI crop image analysis  
- 🤖 OpenAI-powered responses
- 🌧️ Rainwater harvesting system integrated with soil sensors
- 💧 Smart irrigation control based on real-time soil moisture data
- 🧪 Pesticide control system for efficient crop protection
- 📡 IoT cloud integration for remote monitoring and control
- 📊 Real-time data tracking and decision making

---


## 🛠️ Tech Stack

**Backend:** Python, Flask  
**Frontend:** HTML, CSS, JavaScript  
**Database:** SQLite / MySQL  
**AI:** OpenAI API (Chat + Vision)  
**IoT & Hardware:** Arduino / Raspberry Pi, Soil Moisture Sensor, Rain Sensor, Irrigation System, Pesticide Control  
**Cloud:** IoT Cloud (ThingSpeak / Firebase / Blynk)  
**Tools:** GitHub, VS Code, Arduino IDE  

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
    A[User / Farmer] --> B[Web App Interface]

    B --> C{Input Type}

    C -->|Text Query| D[Flask Backend]
    C -->|Image Upload| E[Image Processing]

    D --> F[OpenAI Chat API]
    E --> G[OpenAI Vision API]

    F --> H[Generate Response]
    G --> H

    H --> I[Translate (EN / HI / PA)]
    I --> J[Display to User]

    %% IoT Agribot Flow
    K[Soil & Rain Sensors] --> L[Microcontroller]
    L --> M{Condition Check}

    M -->|Low Moisture| N[Activate Irrigation]
    M -->|Rain Detected| O[Rainwater Harvesting]
    M -->|Pest Detected| P[Pesticide Control]

    N --> Q[Update IoT Cloud]
    O --> Q
    P --> Q

    Q --> B
```
---
## 🔄 System Architecture
```mermaid
graph LR
    %% User Layer
    A[User / Farmer] --> B[Frontend (HTML, CSS, JS)]

    %% Backend Layer
    B --> C[Flask Backend (Python)]

    %% AI Services
    C --> D[OpenAI Chat API]
    C --> E[OpenAI Vision API]

    %% Database
    C --> F[(Database - SQLite/MySQL)]

    %% IoT Layer
    G[Soil Moisture Sensor]
    H[Rain Sensor]
    I[Pesticide Control System]

    G --> J[Microcontroller (Arduino/Raspberry Pi)]
    H --> J
    I --> J

    %% IoT Cloud
    J --> K[IoT Cloud (ThingSpeak / Firebase / Blynk)]

    %% Integration Back to App
    K --> C
    C --> B
```
---

##⚙️ Run Locally
git clone https://github.com/yourusername/Agri_Chatbot.git
```python
pip install -r requirements.txt
python app.py
```
👉 Runs on: http://127.0.0.1:5000
---


##🚀 Future Work
- 📱 Mobile app
- 🌱 Better crop detection
- 📊 Analytics dashboard
---

##👨‍💻 Author
- Gurleen Kaur Bedi
  
---

##📜 License

MIT License
