# 🏦 Loan Approval Prediction App (Flask)

This is a machine learning-based application that predicts whether a loan application is likely to be approved. The app is available in two flavors:
- ✅ Flask Web App
- ✅ Streamlit Interactive App

---

## 📦 Project Structure

```

loan\_classifier\_project/
│
├── models/
│   └── final\_model.pkl                # Trained XGBoost model
│
├── flask\_app/
│   └── app.py                         # Flask web application
│   └── templates/
│       └── index.html                 # HTML form for input
│
├── streamlit\_app.py                   # Streamlit-based UI
├── requirements.txt                   # Python dependencies
├── README.md                          # This file
└── .gitignore                         # Git ignore rules

````

---

## 🚀 Getting Started

### ✅ Clone the repository

```bash
git clone https://github.com/yourusername/loan_classifier_project.git
cd loan_classifier_project
````

---

## 🧠 Model

* Trained using **XGBoost Classifier**.
* Evaluated with metrics such as precision, recall, F1-score.
* Input features include:

  * `Gender`, `Married`, `Dependents`, `Education`, `Self_Employed`
  * `ApplicantIncome`, `CoapplicantIncome`, `LoanAmount`, `Loan_Amount_Term`, `Credit_History`, `Property_Area`

---

## 📌 Dependencies

Make sure to install dependencies inside a virtual environment (recommended):

```bash
pip install -r requirements.txt
```

Or manually install key packages:

```bash
pip install streamlit flask xgboost scikit-learn pandas numpy joblib
```

---

## 🖥️ Streamlit Version

### ▶️ Run the Streamlit app:

```bash
streamlit run streamlit_app.py
```

### 🌐 Features:

* User-friendly interface
* Real-time loan prediction
* Interactive inputs
* Optimized for fast local deployment

---

## 🌐 Flask Version

### ▶️ Run the Flask app:

```bash
cd flask_app
python app.py
```

Then open your browser at: `http://127.0.0.1:5000`

### 🧾 Flask Form Page:

* Simple HTML form
* Accepts all required inputs
* Displays loan approval result

---

## ⚠️ Note on Pickle Compatibility

If you face model loading issues:

* Make sure `xgboost` is installed in the same Python environment.
* Avoid switching Python versions between training and deployment.
* Re-export the model with `Booster.save_model()` if necessary.

---

## 📬 Contact

**Author:** Adarsh Suradkar
📧 \[[YourEmail@example.com](mailto:YourEmail@example.com)]
🔗 [LinkedIn](https://linkedin.com/in/yourprofile)

---

## 📜 License

This project is licensed under the MIT License. See `LICENSE` file for details.

````

---

### ✅ Bonus Tip

Also create a `requirements.txt` file to pin your dependencies:

```txt
streamlit
flask
xgboost
scikit-learn
pandas
numpy
joblib
````

