# 📊 Customer Review Sentiment Analyzer

![Python](https://img.shields.io/badge/Python-3.14-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-WebApp-black?logo=flask)
![Scikit-Learn](https://img.shields.io/badge/ML-Scikit--Learn-orange?logo=scikitlearn)
![Status](https://img.shields.io/badge/Project-Completed-brightgreen)
![License](https://img.shields.io/badge/License-Educational-lightgrey)

---

## 📌 Overview
The **Customer Review Sentiment Analyzer** is a web-based application that uses **Machine Learning and Natural Language Processing (NLP)** to classify customer reviews into **Positive, Negative, and Neutral** sentiments.

This project demonstrates a complete end-to-end ML pipeline, including data generation, preprocessing, model training, and deployment using a Flask web application.

---

## 🚀 Features
- 🔍 Analyze customer reviews in real-time  
- 😊 Classifies sentiment as Positive, Neutral, or Negative  
- ⚡ Fast prediction using trained ML model  
- 🧠 Hybrid approach (Machine Learning + Rule-based)  
- 🌐 Simple and user-friendly web interface  

---

## 🛠️ Technologies Used
- Python  
- Pandas  
- Scikit-learn  
- Flask  
- HTML, CSS  

---

## 📂 Project Structure

sentiment-analysis/
│── app.py
│── train_model.py
│── generate_dataset.py
│── sentiment_model.pkl
│── sentiment_dataset_3000.csv
│── templates/
│ └── index.html
│── static/
│ └── style.css
│── README.md


---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

git clone https://github.com/your-username/sentiment-analysis.git

cd sentiment-analysis


### 2️⃣ Install dependencies

python -m pip install pandas flask scikit-learn


### 3️⃣ Train the model

python train_model.py


### 4️⃣ Run the application

python app.py


---

## 🌐 Usage
1. Open your browser  
2. Go to: http://127.0.0.1:5000/  
3. Enter a customer review  
4. Click submit  
5. View predicted sentiment  

---

## 📊 Model Details
- **Algorithm:** Linear Support Vector Machine (LinearSVC)  
- **Feature Extraction:** TF-IDF Vectorizer  
- **Dataset Size:** 3000 synthetic reviews  
- **Classes:** Positive, Negative, Neutral  

---

## 📈 Results
- High accuracy for long and descriptive reviews  
- TF-IDF improves feature extraction  
- Rule-based fallback enhances short text prediction  

---

## 🔮 Future Scope
- Use real-world datasets (Amazon, Twitter)  
- Implement deep learning models (LSTM, BERT)  
- Add multilingual support  
- Improve UI/UX  
- Deploy on cloud platforms  

---

## 👩‍💻 Author
**Bhavana D.N**

---

## 📜 License
This project is for educational purposes only.

---

## ⭐ Acknowledgements
- Scikit-learn Documentation  
- Flask Documentation  
- NLP learning resources  
