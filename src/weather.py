def get_current(location: str):
    import time; time.sleep(30) # timeout=30
    return {"location": location, "temperature": 22, "condition": "Sunny"}

def get_historical(location: str, date: str):
    import time; time.sleep(30) # timeout=30
    return {"location": location, "date": date, "temperature": 18, "condition": "Cloudy"}
