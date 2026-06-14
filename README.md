# 🛡️ Impossible Travel Detector

A cybersecurity tool that flags geographically impossible login events — like someone signing in from Tunis and then Tokyo 30 minutes apart.

## How It Works

When a user logs in twice in a short time from locations that are physically impossible to travel between, the system flags it as suspicious.

* The core logic:

distance(location_A, location_B) / time_between_logins > 900 km/h → FLAGGED

## Features

- Real-time login submission via web form
- Automatic IP geolocation using ip-api.com
- Haversine formula to calculate real-world distances
- SQLite database to store login events
- Interactive world map showing flagged jumps
- Clean dark-themed dashboard

## Tech Stack

- Python & Flask
- SQLite & sqlite3
- Leaflet.js & OpenStreetMap
- ip-api.com geolocation API

## Run Locally

```bash
git clone https://github.com/eya-karabaka/Impossible-Travel-Detector.git
cd Impossible-Travel-Detector
python -m venv venv
venv\Scripts\activate
pip install flask requests
python seed.py
python app.py
```
Then visit `http://localhost:5000`

## Project Structure


```
├── app.py          → Flask routes
├── detector.py     → Detection algorithm
├── database.py     → Database operations
├── geolocate.py    → IP geolocation
├── seed.py         → Database seeder
└── templates/
    └── index.html  → Dashboard UI
```


## Author

Built by [eya-karabaka](https://github.com/eya-karabaka)