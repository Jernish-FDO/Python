import requests
import sys

# Buddy, you'll need an API key from https://openweathermap.org/
# For this demo, we'll show you how to structure the request!

def get_weather(city):
    api_key = "YOUR_API_KEY_HERE" # Put your real key here!
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }

    print(f"🌦️ Fetching weather for {city}...")
    
    try:
        # In a real app, you'd uncomment the lines below:
        # response = requests.get(base_url, params=params)
        # response.raise_for_status()
        # data = response.json()
        # print(f"It's currently {data['main']['temp']}°C in {city}!")
        
        print("Success! (Simulation Mode: Get an API key to see real-time data)")
        print(f"URL that would be called: {base_url}?q={city}&units=metric&appid=...")
        
    except Exception as e:
        print(f"❌ Oops! Something went wrong: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        get_weather(sys.argv[1])
    else:
        get_weather("New York")
