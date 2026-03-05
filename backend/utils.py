import requests

API_KEY = "4f5724ea4aac9b149bcf422ab73f9960"

def get_weather(city: str):

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)
    data = response.json()

    if response.status_code != 200:
        raise Exception(data.get("message", "Weather API error"))

    return {
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "wind_speed": data["wind"]["speed"],
        "uv_index": 5
    }