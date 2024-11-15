from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load the models
with open('diabetes_model.pkl', 'rb') as file:
    diabetes_model = pickle.load(file)

with open('heart_disease_model.pkl', 'rb') as file:
    heart_disease_model = pickle.load(file)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/diabetes', methods=['GET', 'POST'])
def diabetes_prediction():
    diab_diagnosis = ""
    if request.method == 'POST':
        # Extracting features from the form data
        features = [
            request.form.get('Pregnancies'),
            request.form.get('Glucose'),
            request.form.get('BloodPressure'),
            request.form.get('SkinThickness'),
            request.form.get('Insulin'),
            request.form.get('BMI'),
            request.form.get('DiabetesPedigreeFunction'),
            request.form.get('Age')
        ]
        features = [float(x) for x in features]
        prediction = diabetes_model.predict([features])
        diab_diagnosis = 'The person is diabetic' if prediction[0] == 1 else 'The person is not diabetic'

    return render_template('diabetes.html', result=diab_diagnosis)

@app.route('/heart_disease', methods=['GET', 'POST'])
def heart_disease_prediction():
    heart_diagnosis = ""
    if request.method == 'POST':
        # Extracting features from the form data
        features = [
            request.form.get('age'),
            request.form.get('sex'),
            request.form.get('cp'),
            request.form.get('trestbps'),
            request.form.get('chol'),
            request.form.get('fbs'),
            request.form.get('restecg'),
            request.form.get('thalach'),
            request.form.get('exang'),
            request.form.get('oldpeak'),
            request.form.get('slope'),
            request.form.get('ca'),
            request.form.get('thal')
        ]
        features = [float(x) for x in features]
        prediction = heart_disease_model.predict([features])
        heart_diagnosis = 'The person has heart disease' if prediction[0] == 1 else 'The person does not have heart disease'

    return render_template('heart_disease.html', result=heart_diagnosis)

if __name__ == '__main__':
    app.run(debug=True)
