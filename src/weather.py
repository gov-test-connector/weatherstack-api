def get_current(location: str):
    import time; time.sleep(10) # timeout=10
    return {"location": location, "temperature": 22, "condition": "Sunny"}

def get_historical(location: str, date: str):
    import time; time.sleep(10) # timeout=10
    return {"location": location, "date": date, "temperature": 18, "condition": "Cloudy"}
