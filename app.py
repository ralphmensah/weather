from flask import Flask,render_template
import requests

app = Flask(__name__)



@app.route("/")
def index():
    return render_template("getweather.html")

if __name__=='__main__':
    app.run(debug=True, host='localhost')