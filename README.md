# 🌡️ AI Urban Heat Stress Predictor

An AI-powered system that predicts **heat stress risk for urban workers** using real-time weather data and personal health factors.
The system combines **Machine Learning, FastAPI, and Streamlit** to provide real-time alerts and risk prediction.

---

## 📌 Project Overview

Urban workers such as **delivery personnel, construction workers, street vendors, and traffic police** are exposed to high temperatures for long periods. Excessive heat can cause:

* Heat exhaustion
* Dehydration
* Increased heart rate
* Blood pressure variation
* Heat stroke

This project predicts **heat stress risk levels** using environmental data and personal factors to help prevent health emergencies.

---

## 🎯 Objectives

* Predict **personalized heat stress risk**
* Integrate **weather data API**
* Provide **real-time alerts**
* Build an **AI-driven health monitoring system**
* Create an interactive **dashboard for visualization**

---

## 🧠 Technologies Used

| Technology      | Purpose                |
| --------------- | ---------------------- |
| Python          | Programming language   |
| FastAPI         | Backend API service    |
| Streamlit       | Frontend dashboard     |
| Scikit-learn    | Machine learning model |
| Pandas & NumPy  | Data processing        |
| OpenWeather API | Real-time weather data |
| Joblib          | Model serialization    |

---

## 📂 Project Structure

```
ai-urban-heat-stress-predictor
│
├── backend
│   ├── app.py
│   ├── utils.py
│   └── requirements.txt
│
├── frontend
│   ├── app.py
│   └── requirements.txt
│
├── model
│   └── heat_stress_model.pkl
│
├── data
│   └── heat_stress_dataset.csv
│
├── notebooks
│   ├── week1_dataset_creation.ipynb
│   ├── week1_eda.ipynb
│   └── week1_model_training.ipynb
│
├── tests
│
├── README.md
└── .gitignore
```

---

## ⚙️ How the System Works

```
User Input
   ↓
Streamlit Dashboard
   ↓
FastAPI Backend API
   ↓
Weather Data (OpenWeather API)
   ↓
Machine Learning Model
   ↓
Heat Stress Risk Prediction
```

The system analyzes:

* Temperature
* Humidity
* Wind speed
* UV index
* Age
* Working hours
* Hydration level

---

## 🚀 Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/yourusername/ai-urban-heat-stress-predictor.git
cd ai-urban-heat-stress-predictor
```

### 2️⃣ Create virtual environment

```bash
python -m venv venv
```

Activate environment

Windows:

```bash
venv\Scripts\activate
```

Mac/Linux:

```bash
source venv/bin/activate
```

---

### 3️⃣ Install dependencies

```bash
pip install -r backend/requirements.txt
pip install -r frontend/requirements.txt
```

---

## ▶️ Run the Backend

```bash
uvicorn backend.app:app --reload
```

API will start at:

```
http://127.0.0.1:8000
```

Swagger API documentation:

```
http://127.0.0.1:8000/docs
```

---

## ▶️ Run the Frontend Dashboard

```bash
streamlit run frontend/app.py
```

Dashboard will open at:

```
http://localhost:8501
```

---

## 📊 Example Prediction

Input:

```
City: Delhi
Age: 30
Working Hours: 8
Hydration Level: 3
```

Output:

```
Temperature: 30.7°C
Humidity: 17%
Risk Score: 20.9
Category: Safe
```

---

## 📈 Future Improvements

* Real-time **heat risk alerts**
* Mobile application integration
* Wearable device health monitoring
* Geographic heat maps
* Personalized hydration recommendations

---

## 👨‍💻 Author

**Ruchitha B**

AI / Data Science Enthusiast

---

## 📜 License

This project is open-source and available under the MIT License.
