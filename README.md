# SmartCampus AI
Intelligent Student Risk Prediction System using Machine Learning

---

## Overview

SmartCampus AI is a Machine Learning–powered academic monitoring system built using Python and Flask.

The application predicts Students who are at risk of academic failure by analyzing key academic indicators such as:

- Attendance Percentage  
- Internal Assessment Marks  
- Assignment Scores  

This project demonstrates how Artificial Intelligence can be integrated into web applications to create data-driven early warning systems for educational institutions.

---

## Objectives

- Detect academically at-risk students early  
- Provide AI-driven academic insights  
- Demonstrate full-stack and Machine Learning integration  
- Build a scalable academic intelligence prototype  

---

## System Workflow

User Login  
↓  
Dashboard Input (Attendance, Marks, Assignments)  
↓  
Machine Learning Model (Random Forest)  
↓  
Risk Classification Output  
↓  
Decision Support Insight  

---

## Features

- Secure Authentication System  
- Machine Learning Risk Prediction  
- Academic Risk Classification (High / Low Risk)  
- SQLite Database Integration  
- Modern Responsive UI  
- Automatic Model Training on First Run  
- Modular Multi-File Flask Architecture  

---

## Technology Stack

Backend: Python, Flask  
Machine Learning: Scikit-learn (Random Forest Classifier)  
Database: SQLite  
Data Processing: Pandas, NumPy  
Frontend: HTML, CSS  

---

## Project Structure

smartcampus_ai/

│  
├── app.py  
├── model.py  
├── database.py  
├── requirements.txt  
│  
├── templates/  
│   ├── login.html  
│   └── dashboard.html  
│  
└── static/  
    └── style.css  

---

## Installation Guide

### 1. Clone Repository

git clone https://github.com/YOUR_USERNAME/smartcampus-ai.git  
cd smartcampus-ai  

### 2. Create Virtual Environment (Recommended)

python -m venv venv  
venv\Scripts\activate   (Windows)  

OR  

source venv/bin/activate   (Mac/Linux)  

### 3. Install Dependencies

pip install -r requirements.txt  

### 4. Run Application

python app.py  

Open in browser:

http://127.0.0.1:5000  

---

## Default Login Credentials

Username: admin  
Password: 1234  

---

## Machine Learning Model

The system uses a Random Forest Classifier trained on sample academic performance data.

The model evaluates:

- Attendance trends  
- Internal examination performance  
- Assignment completion consistency  

It classifies students into:

- Low Academic Risk  
- High Academic Risk  

This predictive mechanism supports proactive academic intervention.

---

## Real-World Applicability

This project simulates an AI-driven academic intelligence system that can be adapted for institutions such as:

- SRM Institute of Science and Technology  
- MIT (Massachusetts Institute of Technology)  

The architecture can be extended into a scalable Digital Campus Intelligence Platform.

---

## Future Enhancements

- Risk Probability Score Output  
- Analytics Dashboard with Visualization  
- Password Hashing and Role-Based Access  
- PostgreSQL Integration  
- Cloud Deployment  
- Advanced ML Models (XGBoost / Neural Networks)  

---

## Author

Mohamed Mustak M  
AI and Full-Stack Developer  

Focused on building intelligent systems that combine Machine Learning with scalable web technologies.

---

## License

This project is developed for educational and research purposes.
