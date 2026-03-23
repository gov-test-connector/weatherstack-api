from src.weather import get_historical

def test_historical_weather_returns_dict():
    result = get_historical("London", "2023-01-01")
    assert isinstance(result, dict)

def test_historical_weather_content():
    result = get_historical("London", "2023-01-01")
    assert result["location"] == "London"
    assert result["date"] == "2023-01-01"
