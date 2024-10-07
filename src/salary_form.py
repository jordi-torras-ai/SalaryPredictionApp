from flask import Flask, render_template, request
import joblib
import os

# Load the saved model
model = joblib.load('../model/Salary_model.pkl')

# Set the template folder to the new path
template_dir = os.path.abspath('../templates')

# Initialize the Flask application with the custom template folder
app = Flask(__name__, template_folder=template_dir)

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
