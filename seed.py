import json
from database import init_db, insert_login

def seed():
    init_db()
    with open("data/logins.json") as f:
        data = json.load(f)
    
    for login in data["logins"]:
        insert_login(
            user=login["user"],
            ip=login["ip"],
            city=login["city"],
            lat=login["lat"],
            lon=login["lon"],
            timestamp=login["timestamp"]
        )
    print("Database seeded successfully!")

seed()