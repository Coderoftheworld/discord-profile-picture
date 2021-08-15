from flask import Flask, render_template

app = Flask(__name__)

# Web Page
@app.route("/")
def hello():
    return render_template('index.html')

# RESTful api endpoint
@app.route("/scrape", methods=["POST"])
def scrape():
    pass

if __name__ == "__main__":
    app.run(debug=True)
