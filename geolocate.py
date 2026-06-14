import requests

def geolocate(ip):
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}")
        data = response.json() 
        if data["status"] == "success":
            return data["city"], data["lat"], data["lon"]
        else:
            return "Unknown", 0.0, 0.0
    except:
        return "Unknown", 0.0, 0.0