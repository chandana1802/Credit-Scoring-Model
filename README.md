# 💳 Credit Scoring Model

A Machine Learning-based web application that predicts an individual's creditworthiness based on their financial information.

## 📌 About the Project

The **Credit Scoring Model** uses Machine Learning to analyze financial information such as income, debt, loan amount, payment history, credit history, number of loans, and employment experience.

The system uses a **Random Forest Classifier** to predict whether an applicant is likely to be creditworthy.

The trained model is integrated with a **Flask web application**, where users can enter their financial details and receive a creditworthiness prediction.

## 🎯 Objectives

* Predict an individual's creditworthiness using financial data
* Apply Machine Learning classification techniques
* Analyze financial history and risk factors
* Evaluate model performance
* Build a simple and user-friendly web application

## ✨ Features

* 🤖 Random Forest Machine Learning
* 📊 Financial data analysis
* 💳 Creditworthiness prediction
* 📈 Accuracy evaluation
* 🎯 Precision
* 🔍 Recall
* 📊 F1-Score
* 📉 ROC-AUC
* 🔢 Confusion Matrix
* 🌐 Flask Web Application
* 📱 Responsive User Interface

## 🛠️ Technologies Used

* Python
* Pandas
* Scikit-learn
* Random Forest
* Joblib
* Flask
* HTML
* CSS
* VS Code

## 📂 Project Structure

```text
credit_scoring_project/
│
├── credit_data.csv
├── train_model.py
├── app.py
├── model.pkl
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
```

## 📊 Dataset

The dataset contains financial information about applicants.

### Features

| Feature          | Description                         |
| ---------------- | ----------------------------------- |
| Age              | Applicant's age                     |
| Income           | Applicant's income                  |
| Debt             | Existing debt                       |
| Loan Amount      | Requested loan amount               |
| Credit History   | Length of credit history            |
| Payment History  | Percentage of payments made on time |
| Number of Loans  | Number of existing loans            |
| Employment Years | Years of employment                 |
| Creditworthy     | Target variable                     |

### Target Variable

* `0` → Not Creditworthy
* `1` → Creditworthy

## 🧠 Machine Learning Model

The project uses the **Random Forest Classifier**.

Random Forest is an ensemble Machine Learning algorithm that combines multiple Decision Trees to make a final prediction.

### Workflow

```text
Dataset
   ↓
Data Preprocessing
   ↓
Feature Selection
   ↓
Train-Test Split
   ↓
Random Forest Training
   ↓
Model Evaluation
   ↓
Save Trained Model
   ↓
Flask Web Application
   ↓
Creditworthiness Prediction
```

## 📈 Model Evaluation

The model is evaluated using:

* **Accuracy** – Measures the overall percentage of correct predictions.
* **Precision** – Measures how many predicted creditworthy applicants are actually creditworthy.
* **Recall** – Measures how many actual creditworthy applicants are correctly identified.
* **F1-Score** – Combines Precision and Recall.
* **ROC-AUC** – Measures how well the model distinguishes between the two classes.
* **Confusion Matrix** – Shows correct and incorrect classifications.

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/chandana1802/credit-scoring-model.git
```

### 2. Open the Project

```bash
cd credit-scoring-model
```

### 3. Install Required Libraries

```bash
python -m pip install flask pandas scikit-learn joblib
```

For Windows, if `python` doesn't work:

```bash
py -m pip install flask pandas scikit-learn joblib
```

## ▶️ How to Run

### Step 1: Train the Machine Learning Model

```bash
python train_model.py
```

This will train the Random Forest model and create the `model.pkl` file.

### Step 2: Run the Flask Application

```bash
python app.py
```

### Step 3: Open the Application

Open your browser and visit:

```text
http://127.0.0.1:5000
```

## 🔄 Application Workflow

```text
User
 ↓
Enters Financial Information
 ↓
Flask Web Application
 ↓
Random Forest Model
 ↓
Prediction
 ↓
Creditworthy / Not Creditworthy
```

## 🚀 Future Enhancements

* Add Logistic Regression
* Add Decision Tree
* Compare multiple Machine Learning algorithms
* Add interactive graphs and dashboards
* Generate credit scores from 300–850
* Add Low / Medium / High risk classification
* Add feature importance visualization
* Add Explainable AI
* Use a larger real-world dataset
* Add database support
* Add user authentication
* Deploy the application online
* Develop a mobile application

## ⚠️ Disclaimer

This project is developed for **educational and demonstration purposes only**.

The included dataset is a small sample dataset and should not be used for actual lending or financial decisions. A real-world credit scoring system would require large datasets, rigorous validation, fairness testing, security, explainability, and compliance with applicable financial regulations.

## 👩‍💻 Author

**Chandana M M**

Electronics and Communication Engineering Student

### 🔗 Connect With Me

**GitHub:**
[https://github.com/chandana1802](https://github.com/chandana1802)

**LinkedIn:**
[https://www.linkedin.com/in/chandana-mm-05029132/](https://www.linkedin.com/in/chandana-mm-05029132/)

---

⭐ **If you like this project, please give it a star!**
