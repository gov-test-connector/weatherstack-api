def get_current(location: str):
    return {"location": location, "temperature": 22, "condition": "Sunny"}

def get_historical(location: str, date: str):
    return {"location": location, "date": date, "temperature": 18, "condition": "Cloudy"}
