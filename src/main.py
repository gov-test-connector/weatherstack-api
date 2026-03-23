from fastapi import FastAPI
from .weather import get_current, get_historical

app = FastAPI(title="WeatherStack API")

@app.get("/weather/current")
def current_weather(location: str):
    return get_current(location)

@app.get("/weather/historical")
def historical_weather(location: str, date: str):
    return get_historical(location, date)

@app.get("/health")
def health():
    return {"status": "ok"}
