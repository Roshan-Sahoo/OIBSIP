import requests

def get_weather(api_key, location):
    # API URL for current weather
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    
    try:
        # Send a request to the API
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)

        data = response.json()

        # Check if the city is found
        if data["cod"] != 200:
            print(f"Error: {data['message']}")
            return

        # Extract relevant data
        city = data['name']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        weather_description = data['weather'][0]['description']

        # Display the weather information
        print(f"Weather in {city}:")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Condition: {weather_description.capitalize()}")
    
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Error connecting: {conn_err}")
    except requests.exceptions.Timeout as timeout_err:
        print(f"Timeout error: {timeout_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"An error occurred: {req_err}")
    except KeyError as key_err:
        print(f"Unexpected response format: {key_err}")

def main():
    # Your OpenWeatherMap API key
    api_key = "d254e9af606e6ffa5d006f1e6ccaffe3"

    # Prompt the user to enter a location (city or ZIP code)
    location = input("Enter a city name or ZIP code: ")

    # Get and display the weather information
    get_weather(api_key, location)

if __name__ == "__main__":
    main()
