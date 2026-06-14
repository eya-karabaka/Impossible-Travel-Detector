from flask import Flask, render_template, request, redirect, url_for
from database import init_db, get_all_logins, insert_login
from detector import detect
from geolocate import geolocate

app = Flask(__name__) 

@app.route("/") 
def home():
    logins = get_all_logins()
    alerts = detect(logins)
    return render_template("index.html", alerts=alerts)

@app.route("/add", methods=["POST"]) 

def add_login(): 
    user = request.form["user"]
    ip = request.form["ip"]
    raw_timestamp = request.form["timestamp"]
    timestamp = raw_timestamp.replace("T", " ") + ":00"
    city, lat, lon = geolocate(ip)
    insert_login(user, ip, city, lat, lon, timestamp)
    return redirect(url_for("home")) 

if __name__ == "__main__": 
    init_db()
    app.run(debug=True)