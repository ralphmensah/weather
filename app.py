from flask import Flask,render_template,request
from pprint import pprint
import requests
from datetime import datetime
from datetime import timedelta
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    
    try:
        url='http://api.openweathermap.org/data/2.5/weather?q={}&APPID=9a9e6eeb16ffef5a4c5c1ba9bf0bffc4'
    # city = "Accra"
    
        data=[]
        if request.method == 'POST':
            city = str(request.form.get('city').capitalize())
    
            request_url = (requests.get(url.format(city))).json()
        
            weather = {
                "city": city,
                "temperature":request_url["main"]["temp"],
                "discription":request_url["weather"][0]["description"],
                "icon": request_url["weather"][0]["icon"]
                    }
            data.append(weather)
    except:
        pass
    
        
    return render_template("index.html",  data = data)



if __name__=='__main__':
    app.run(debug=True)
