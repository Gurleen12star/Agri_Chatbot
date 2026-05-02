# 🌾 AgriSahayta – Smart Farming Assistant with IOT Monitoring 
-->AgriCSahayta is an integrated AI + IoT smart agriculture system designed to assist farmers in making informed, real-time decisions. The project combines a web-based intelligent chatbot with a hardware-driven agribot ecosystem to address key challenges in modern farming such as irrigation management, crop health monitoring, and resource optimization.

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
**Frontend:** Next.JS  
**Database:** SUPABASE 
**AI:** OpenAI API (Chat + Vision) + Random Forest and XGBoost 
**IoT & Hardware:** ESP32, Soil Moisture Sensor, Rain Sensor, Irrigation System, Pesticide Control  
**Cloud:** IoT Cloud (Firebase and Ubidots)  
**Tools:** GitHub, VS Code, Arduino IDE  

---

## 🖼 Screenshots
<img width="772" height="573" alt="Screenshot 2026-04-24 134326" src="https://github.com/user-attachments/assets/edfa4619-74a5-473c-be5c-b3e2600794ec"  width="100%"/>
<img src="https://github.com/user-attachments/assets/104e31dd-ea73-47b0-959c-411ce10fb48e" width="100%" />
<img src="https://github.com/user-attachments/assets/3b6aab74-2416-4525-b673-fd75eb5dec7e" width="100%" />
<img src="https://github.com/user-attachments/assets/98ca8f5e-8611-4be1-b9e4-06948a8e5c33" width="100%" />
<img src="https://github.com/user-attachments/assets/f43d735a-0e6d-4cde-9d71-7fd472dbe7e7" width="100%" />
<img src="https://github.com/user-attachments/assets/8e6c1c1e-ae1a-4e11-8a9c-055861c6edc5" width="100%" />

---

## ⚙️ How It Works

1. User logs in through the web interface  
2. User interacts with the system by:
   - Sending a text query, or  
   - Uploading a crop image  

3. Flask backend processes the request  

4. Based on input:
   - Text queries → processed using OpenAI Chat API  
   - Images → analyzed using OpenAI Vision API  

5. AI generates a response and translates it into the selected language (English, Hindi, Punjabi)  
6. Response is displayed to the user  

7. Meanwhile, IoT sensors (soil moisture, rain, etc.) continuously collect field data  
8. Microcontroller analyzes sensor data and checks conditions  

9. Based on conditions:
   - Low moisture → irrigation system activated  
   - Rain detected → rainwater harvesting triggered  
   - Pest detected → pesticide control system activated  

10. Sensor data is sent to the IoT cloud platform  
11. Cloud updates are reflected in the application/dashboard for remote monitoring


---

## 🔄 Workflow

```mermaid
flowchart TD
    A[User Farmer] --> B[Web App Interface]

    B --> C{Input Type}

    C -->|Text Query| D[Flask Backend]
    C -->|Image Upload| E[Image Processing]

    D --> F[OpenAI Chat API]
    E --> G[OpenAI Vision API]

    F --> H[Generate Response]
    G --> H

    H --> I[Translate EN HI PA]
    I --> J[Display to User]

    %% IoT Agribot Flow
    K[Soil and Rain Sensors] --> L[Microcontroller]
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
    A[User Farmer] --> B[Frontend HTML CSS JS]

    B --> C[Flask Backend Python]

    C --> D[OpenAI Chat API]
    C --> E[OpenAI Vision API]

    C --> F[(Database SQLite MySQL)]

    G[Soil Moisture Sensor] --> H[Microcontroller Arduino RaspberryPi]
    I[Rain Sensor] --> H
    J[Pesticide System] --> H

    H --> K[IoT Cloud ThingSpeak Firebase Blynk]

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
