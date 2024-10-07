from flask import Flask, render_template, request

app = Flask(__name__)

# Route for the form
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the text input from the form
        user_text = request.form['text_input']
        return f"Your text field was: {user_text}"
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
