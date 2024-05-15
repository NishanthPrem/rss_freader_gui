import feedparser

from flask import Flask, render_template, request
from urllib.parse import urlparse
app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        try:
            # Get input from the user and parse it
            user_input = request.form['input']
            url_data = urlparse(user_input)

            """
            `scheme`: protocol used 'http' or 'https'
            `netloc`:   contains the network location of the resource.
            """
            if not (url_data.scheme and url_data.netloc):  
                raise ValueError()   # Raise error if invalid URL
            output = {}
            feed = feedparser.parse(user_input)
            for entry in feed.entries:
                output["Title"] = entry.title
                output["Link"] = entry.links
                output["Description"] = entry.description
            return f"{output}"

        except Exception as e:
            return f"Invalid URL, {e}"


if __name__ == '__main__':
    app.run(debug=True)
