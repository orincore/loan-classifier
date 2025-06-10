from flask import Flask, request, render_template
import numpy as np
import joblib
import os

app = Flask(__name__)
model = joblib.load('models/final_model.pkl')

# Manual encodings
mapping = {
    'Male': 1, 'Female': 0,
    'Yes': 1, 'No': 0,
    'Graduate': 1, 'Not Graduate': 0,
    'Urban': 2, 'Rural': 0, 'Semiurban': 1,
    '0': 0, '1': 1, '2': 2, '3+': 3
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        form = request.form
        features = [
            mapping[form['Gender']],
            mapping[form['Married']],
            mapping[form['Dependents']],
            mapping[form['Education']],
            mapping[form['Self_Employed']],
            float(form['ApplicantIncome']),
            float(form['CoapplicantIncome']),
            float(form['LoanAmount']),
            float(form['Loan_Amount_Term']),
            float(form['Credit_History']),
            mapping[form['Property_Area']]
        ]

        prediction = model.predict([features])[0]
        result = "✅ Loan Approved" if prediction == 1 else "❌ Loan Rejected"
        return render_template('index.html', prediction=result)
    
    except Exception as e:
        return render_template('index.html', prediction=f"⚠️ Error: {e}")

if __name__ == '__main__':
    app.run(debug=True)
