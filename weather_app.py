import os
import requests


API_KEY = os.getenv("OPENWEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city):
    if not API_KEY:
        print("Error: OPENWEATHER_API_KEY is not set.")
        return

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
        data = response.json()

        if response.status_code == 200:
            print("\n===== Weather Information =====")
            print("City:", data["name"])
            print("Temperature:", data["main"]["temp"], "°C")
            print("Feels Like:", data["main"]["feels_like"], "°C")
            print("Humidity:", data["main"]["humidity"], "%")
            print("Weather:", data["weather"][0]["description"].title())
            print("Wind Speed:", data["wind"]["speed"], "m/s")

        elif response.status_code == 404:
            print("City not found. Please check the city name.")

        else:
            print("Unable to fetch weather data.")

    except requests.exceptions.RequestException as error:
        print("Network error:", error)


def main():
    print("===== Live Weather App =====")

    while True:
        city = input("\nEnter city name (or type 'exit' to quit): ")

        if city.lower() == "exit":
            print("Goodbye!")
            break

        if not city.strip():
            print("Please enter a city name.")
            continue

        get_weather(city)


if __name__ == "__main__":
    main()
