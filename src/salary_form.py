from flask import Flask, render_template, request
import joblib

# Load the saved model
model = joblib.load('../model/Salary_model.pkl')

# Initialize the Flask application
app = Flask(__name__)

# Define the home route to show the input form
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get the years of experience from the form
        years_experience = float(request.form["years_experience"])
        
        # Predict the salary using the loaded model
        predicted_salary = model.predict([[years_experience]])[0]
        
        # Display the result
        return render_template("result.html", salary=round(predicted_salary, 2), years_experience=years_experience)
    
    # Render the input form template
    return render_template("index.html")

# Run the application
if __name__ == "__main__":
    app.run(debug=True)
