from flask import Flask,render_template,request,url_for,flash,redirect
import requests
from datetime import datetime,timedelta
app = Flask(__name__)

app.config['SECRET_KEY'] = '16e6f9980e1feee2ebe8dad714089a3589fd42ab'

@app.route("/home", methods=['GET', 'POST'])
@app.route("/", methods=['GET', 'POST'])
def index():
    # form = NewForm()
    try:
        url='http://api.openweathermap.org/data/2.5/weather?q={}&APPID=9a9e6eeb16ffef5a4c5c1ba9bf0bffc4&units=metric'
        # city = "Accra"
        data=[]
        if request.method == 'POST':
            city = str(request.form.get('city').capitalize())
            request_url = (requests.get(url.format(city))).json()
            weather = {
                "city": city,
                "temperature":round(request_url["main"]["temp"]),
                "discription":request_url["weather"][0]["description"],
                "icon": request_url["weather"][0]["icon"]
                    }
            data.append(weather)
    
    except:
        
        flash(f'Weather Information not Found for {city.title()}')
        return redirect(url_for('index'))

    return render_template("index.html",  data = data)
    

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404page.html", title="404 page")


@app.errorhandler(500) 
def server_failure(e):
    render_template("<h1>server failure</h1>") 


if __name__=='__main__':
    app.run(debug=True)
