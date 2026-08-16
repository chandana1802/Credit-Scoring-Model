from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Load trained model
model = joblib.load("model.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    try:
        age = float(request.form["age"])
        income = float(request.form["income"])
        debt = float(request.form["debt"])
        loan_amount = float(request.form["loan_amount"])
        credit_history_years = float(
            request.form["credit_history_years"]
        )
        payment_history = float(
            request.form["payment_history"]
        )
        number_of_loans = float(
            request.form["number_of_loans"]
        )
        employment_years = float(
            request.form["employment_years"]
        )

        # Create dataframe
        input_data = pd.DataFrame([{
            "age": age,
            "income": income,
            "debt": debt,
            "loan_amount": loan_amount,
            "credit_history_years": credit_history_years,
            "payment_history": payment_history,
            "number_of_loans": number_of_loans,
            "employment_years": employment_years
        }])

        # Prediction
        prediction = model.predict(input_data)[0]

        # Probability
        probability = model.predict_proba(input_data)[0][1]

        credit_score = int(probability * 100)

        if prediction == 1:
            result = "Creditworthy"
            message = "The applicant has a good credit profile."
        else:
            result = "Not Creditworthy"
            message = "The applicant may have a higher credit risk."

        return render_template(
            "index.html",
            result=result,
            message=message,
            credit_score=credit_score
        )

    except Exception as e:
        return render_template(
            "index.html",
            result="Error",
            message=str(e)
        )


if __name__ == "__main__":
    app.run(debug=True)