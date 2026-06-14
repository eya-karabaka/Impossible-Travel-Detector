from database import init_db, insert_login

def seed():
    init_db()

    logins = [
        ("alice", "192.168.1.1", "New York", 40.7128, -74.0060, "2024-01-15 08:00:00"),
        ("alice", "203.0.113.5", "Tokyo", 35.6762, 139.6503, "2024-01-15 08:30:00"),
        ("bob", "198.51.100.2", "Paris", 48.8566, 2.3522, "2024-01-15 09:00:00"),
        ("bob", "198.51.100.9", "London", 51.5074, -0.1278, "2024-01-15 12:00:00"),
        ("carol", "10.0.0.5", "Tunis", 36.8065, 10.1815, "2024-01-15 10:00:00"),
        ("carol", "10.0.0.9", "Dubai", 25.2048, 55.2708, "2024-01-15 12:00:00"),
    ]

    for login in logins:
        insert_login(*login)

    print("Database seeded successfully!")

seed()