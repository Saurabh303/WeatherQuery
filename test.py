from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/temperature', methods=['POST'])
def temperature():
    zipcode=request.form['zip']
    #r=requests.get('http://samples.openweathermap.org/data/2.5/weather?zip='+zipcode+',uk&appid=20a7df5e81ed3d83deba9835355ee263')
    r=requests.get('http://api.openweathermap.org/data/2.5/weather?zip='+zipcode+',us&appid=20a7df5e81ed3d83deba9835355ee263')
    #json_object=r.text
    #return json_object
    json_object=r.json()
    k=float(json_object['main']['temp'])
    c=k-273.15
    return render_template('temperature.html',temp=c)


if __name__ == '__main__':
    app.run(debug=True)
