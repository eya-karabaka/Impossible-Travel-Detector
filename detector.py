import json 
from math import radians, sin, cos, sqrt, atan2 
from datetime import datetime

MAX_SPEED_KMH = 900

def haversine(lat1, lon1, lat2, lon2):
    R = 6371
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    return R * c

def load_logins(filepath):
    with open(filepath) as f:
        data = json.load(f)
    return data["logins"]

def detect(logins):
    alerts = []
    by_user = {}

    for login in logins:
        user = login["user"]
        if user not in by_user:
            by_user[user] = []
        by_user[user].append(login)

    for user, events in by_user.items():
        events.sort(key=lambda x: x["timestamp"])
        for i in range(len(events) - 1):
            a = events[i]
            b = events[i+1]
            distance = haversine(a["lat"], a["lon"], b["lat"], b["lon"])
            t1 = datetime.strptime(a["timestamp"], "%Y-%m-%d %H:%M:%S")
            t2 = datetime.strptime(b["timestamp"], "%Y-%m-%d %H:%M:%S")
            hours = (t2 - t1).total_seconds() / 3600
            if hours == 0:
                speed = float('inf')
            else:
                speed = distance / hours
            if speed > MAX_SPEED_KMH:
                alerts.append({
                    "user": user,
                    "from": a["city"],
                    "to": b["city"],
                    "distance_km": round(distance),
                    "time_hours": round(hours, 2),
                    "speed_kmh": round(speed),
                    "from_lat": a["lat"],
                    "from_lon": a["lon"],
                    "to_lat": b["lat"],
                    "to_lon": b["lon"]
                })
    return alerts