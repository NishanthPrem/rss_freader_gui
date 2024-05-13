from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def url():
    if request.method == 'POST':
        input_value = request.form['input']
        return f'The input value is: {input_value}'


if __name__ == '__main__':
    app.run(debug=True)
