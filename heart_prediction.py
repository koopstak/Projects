from flask import Flask, render_template, request, jsonify
import joblib

app = Flask(__name__)
model = joblib.load('random_forest_model.joblib')

# Define the main page route
@app.route('/')
def home():
    return render_template('index.html')

# Define the prediction route
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input data from the form
        age = float(request.form['age'])
        cigsPerDay = float(request.form['cigsPerDay'])
        totChol = float(request.form['totChol'])
        sysBP = float(request.form['sysBP'])
        diaBP = float(request.form['diaBP'])
        BMI = float(request.form['BMI'])
        heartRate = float(request.form['heartRate'])
        glucose = float(request.form['glucose'])

        # Make a prediction using the Random Forest model
        input_data = [[age, cigsPerDay, totChol, sysBP, diaBP, BMI, heartRate, glucose]]
        prediction = int(model.predict(input_data)[0])

        # Return the prediction to the HTML template
        return render_template('index.html', prediction=prediction)

    except Exception as e:
        return render_template('index.html', error=str(e))

if __name__ == '__main__':
    app.run(port=5000)