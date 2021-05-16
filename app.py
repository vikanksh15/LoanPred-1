from flask import Flask, request, render_template
# from flask_cors import cross_origin
import sklearn
import pickle
import pandas as pd

app = Flask(__name__)
model = pickle.load(open("classifier3.pkl", "rb"))


@app.route("/")
# @cross_origin() # Cross-domain access to your web API's
def home():
    return render_template("home.html")

@app.route("/predict", methods = ["GET", "POST"])
# @cross_origin()
def predict():
    if request.method == "POST":
        
        # Applicant's Income
        applicant_income = float(request.form["applicant_income"])
        
        # Co-Applicant's Income
        coapplicant_income = float(request.form["coapplicant_income"])
        
        # Loan Amount
        loan_amount = float(request.form["loan_amount"])
        
        #Loan Amount Term
        loan_amount_term = float(request.form["loan_amount_term"])
        
        # Credit History
        credit_history = float(request.form["credit_history"])
        
        # Gender
        Gender_Male = request.form['Gender_Male']
        if (Gender_Male == 'Male'):
            Gender_Male = 1
        else:
            Gender_Male = 0
            
        # Married Status
        Married = request.form['Married']
        if (Married == '1'):
            Married_Yes = 1
        else:
            Married_Yes = 0
            
        #Number of dependents:
        Dependents = request.form['Dependents']
        if (Dependents == '1'):
            Dependents_1 = 1
            Dependents_2 = 0
            Dependents_3 = 0
        elif (Dependents == '2'):
            Dependents_2 = 1
            Dependents_1 = 0
            Dependents_3 = 0
        elif (Dependents == '3'):
            Dependents_3 = 1
            Dependents_1 = 0
            Dependents_2 = 0
            
        
        
        # Education
        Education_NotGraduate = request.form['Education_NotGraduate']
        if (Education_NotGraduate == '0'):
            Education_NotGraduate = 0
        else:
            Education_NotGraduate = 1
            
        # Self-Employed
        Self_Employed_Yes = request.form['Self_Employed_Yes']
        if (Self_Employed_Yes == '1'):
            Self_Employed_Yes = 1
        else:
            Self_Employed_Yes = 0
            
        # Property Area SemiUrban
        Property_Area_Semiurban = request.form['Property_Area_Semiurban']
        if (Property_Area_Semiurban == 'Semi-Urban'):
            Property_Area_Semiurban = 1
        else:
            Property_Area_Semiurban = 0
            
        #Predictions:
        prediction = model.predict([[
            applicant_income,
            coapplicant_income,
            loan_amount,
            loan_amount_term,
            credit_history,
            Gender_Male,
            Married,
            Dependents,
            Education_NotGraduate,
            Self_Employed_Yes,
            Property_Area_Semiurban
        ]])
        
        output = prediction[0]
        if output == 1:
            return render_template('resultPage.html', prediction_text='You are eligible for a loan!')
        elif output == 0:
            return render_template('resultPage.html', prediction_text='You are not eligible for a loan')


if __name__ == '__main__':
    app.run(debug=True)
            