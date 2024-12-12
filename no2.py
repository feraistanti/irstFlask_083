from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    text_input = request.form.get('text_input')  # Tangkap input dari form
    return f"You entered: {text_input}"

if __name__ == '__main__':
    app.run(debug=True)
