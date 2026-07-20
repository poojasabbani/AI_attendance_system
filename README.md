# 🎓 ATTEND AI

<div align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Web_App-red?logo=streamlit)
![Supabase](https://img.shields.io/badge/Supabase-Database-green?logo=supabase)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer_Vision-blue?logo=opencv)
![License](https://img.shields.io/badge/License-MIT-yellow)

### AI-Powered Smart Attendance Management System

Automatic classroom attendance using **Face Recognition**, **Voice Biometrics**, and **QR-based Subject Enrollment**.

</div>

---

# 📌 Overview

ATTEND AI is an intelligent attendance management platform that automates classroom attendance using Artificial Intelligence.

Students register once by enrolling their facial features and optional voice biometrics. Teachers can then mark attendance automatically from classroom photographs, eliminating manual roll calls and reducing attendance fraud.

The system is built using Streamlit, Supabase, OpenCV, Face Recognition, and Resemblyzer.

---

# ✨ Features

## 👨‍🏫 Teacher

- Secure teacher authentication
- Create and manage subjects
- QR / Join Code based enrollment
- Automatic attendance from classroom photos
- View attendance statistics
- Student management

---

## 👨‍🎓 Student

- Face-based login
- Student registration
- Face embedding generation
- Voice enrollment
- View enrolled subjects
- Attendance history
- Join subjects using QR code

---

## 🤖 AI Features

- Face Detection
- Face Recognition
- Face Embedding Generation
- Voice Embedding Generation
- Multi-face Attendance Detection
- Automatic Attendance Logging

---

# 🏗️ Tech Stack

| Category | Technologies |
|-----------|-------------|
| Frontend | Streamlit |
| Backend | Python |
| Database | Supabase |
| Computer Vision | OpenCV, face_recognition, dlib |
| Speaker Recognition | Resemblyzer |
| Audio Processing | Librosa |
| Machine Learning | Scikit-learn |
| Authentication | bcrypt |
| QR Generation | Segno |

---

# 📂 Project Structure

```text
ATTEND-AI/
│
├── app.py
├── requirements.txt
│
├── src/
│   ├── components/
│   ├── database/
│   ├── pipeline/
│   ├── screens/
│   ├── ui/
│   └── logo.png
│
└── README.md
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/poojasabbani/AI_attendance_system.git

cd AI_attendance_system
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file or configure your database settings.

```
SUPABASE_URL=YOUR_SUPABASE_URL

SUPABASE_KEY=YOUR_SUPABASE_KEY
```

---

# ▶️ Run the Application

```bash
streamlit run app.py
```

---

# 📸 Workflow

## Student Registration

```
Capture Face
        │
        ▼
Generate Face Embedding
        │
        ▼
(Optional)
Record Voice
        │
        ▼
Generate Voice Embedding
        │
        ▼
Store in Supabase
```

---

## Automatic Attendance

```
Teacher Uploads Classroom Photo
               │
               ▼
Face Detection
               │
               ▼
Face Recognition
               │
               ▼
Match Student Embeddings
               │
               ▼
Attendance Logged Automatically
```

---

# 🧠 AI Pipeline

### Face Recognition

- Detect faces
- Extract embeddings
- Compare embeddings
- Identify students
- Mark attendance

---

### Voice Recognition

- Record audio
- Generate speaker embeddings
- Compare cosine similarity
- Verify speaker identity

---

# 🗄 Database

Main tables:

- teachers
- students
- subjects
- subject_students
- attendance_logs

---

# 📊 Future Improvements

- Live Webcam Attendance
- Classroom Video Attendance
- Anti-Spoof Detection
- Liveness Detection
- Attendance Analytics Dashboard
- Email Notifications
- Mobile Application
- Face Mask Recognition
- Voice Attendance Verification

---

# 📷 Screenshots

<img width="490" height="495" alt="image" src="https://github.com/user-attachments/assets/2f7db4e1-f016-4c0b-b4e3-35cd54f29efd" />
<img width="622" height="649" alt="image" src="https://github.com/user-attachments/assets/5df7a0b9-39fe-4cea-9f6e-dcae3082c9ad" />
<img width="590" height="359" alt="image" src="https://github.com/user-attachments/assets/b3442383-7d76-4cf1-9811-ab7552b2a428" />
<img width="359" height="256" alt="image" src="https://github.com/user-attachments/assets/6fb4c05f-72b2-467e-bbe0-bc535dff94a7" />
<img width="617" height="589" alt="image" src="https://github.com/user-attachments/assets/feed8f0a-4555-470d-a013-09f16ed003cb" />
<img width="592" height="396" alt="image" src="https://github.com/user-attachments/assets/b2b0533b-e2cd-4b21-bfe5-7892201198a4" />




---

# 🤝 Contributing

Contributions are welcome.

1. Fork the repository

2. Create a feature branch

```bash
git checkout -b feature-name
```

3. Commit changes

```bash
git commit -m "Added new feature"
```

4. Push branch

```bash
git push origin feature-name
```

5. Open a Pull Request

---

# 📄 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Pooja Sabbani**

Robotics and Automation

DY Patil College of Engineering

---

## ⭐ Support

If you found this project useful, consider giving it a **⭐ Star** on GitHub.
