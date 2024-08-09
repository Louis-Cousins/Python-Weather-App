weather_data = {
    "london": {"temperature": "22°C", "conditions": "Sunny", "wind_speed": "4km/h", "humidity": "50%"},
    "washington, D.C.": {"temperature": "28°C", "conditions": "Partly Cloudy", "wind_speed": "12km/h", "humidity": "60%"},
    "tokyo": {"temperature": "30°C", "conditions": "Humid", "wind_speed": "5km/h", "humidity": "70%"},
    "paris": {"temperature": "24°C", "conditions": "Cloudy", "wind_speed": "10km/h", "humidity": "55%"},
    "berlin": {"temperature": "19°C", "conditions": "Rainy", "wind_speed": "14km/h", "humidity": "80%"},
    "beijing": {"temperature": "31°C", "conditions": "Sunny", "wind_speed": "6km/h", "humidity": "40%"},
    "canberra": {"temperature": "15°C", "conditions": "Windy", "wind_speed": "20km/h", "humidity": "65%"},
    "ottawa": {"temperature": "18°C", "conditions": "Overcast", "wind_speed": "8km/h", "humidity": "70%"},
    "brasília": {"temperature": "25°C", "conditions": "Rainy", "wind_speed": "11km/h", "humidity": "85%"},
    "new Delhi": {"temperature": "35°C", "conditions": "Hot", "wind_speed": "7km/h", "humidity": "45%"},
    "buenos Aires": {"temperature": "17°C", "conditions": "Clear", "wind_speed": "5km/h", "humidity": "60%"},
    "mexico City": {"temperature": "22°C", "conditions": "Thunderstorms", "wind_speed": "9km/h", "humidity": "75%"},
    "jakarta": {"temperature": "29°C", "conditions": "Humid", "wind_speed": "5km/h", "humidity": "80%"},
    "Cairo": {"temperature": "34°C", "conditions": "Hot", "wind_speed": "10km/h", "humidity": "35%"},
    "nairobi": {"temperature": "23°C", "conditions": "Partly Cloudy", "wind_speed": "7km/h", "humidity": "55%"},
    "helsinki": {"temperature": "12°C", "conditions": "Chilly", "wind_speed": "15km/h", "humidity": "65%"},
    "bangkok": {"temperature": "32°C", "conditions": "Humid", "wind_speed": "8km/h", "humidity": "80%"},
    "riyadh": {"temperature": "39°C", "conditions": "Very Hot", "wind_speed": "9km/h", "humidity": "20%"},
    "rome": {"temperature": "26°C", "conditions": "Sunny", "wind_speed": "6km/h", "humidity": "50%"},
    "madrid": {"temperature": "27°C", "conditions": "Sunny", "wind_speed": "10km/h", "humidity": "40%"},
    "lisbon": {"temperature": "24°C", "conditions": "Clear", "wind_speed": "12km/h", "humidity": "55%"},
    "pretoria": {"temperature": "20°C", "conditions": "Partly Cloudy", "wind_speed": "10km/h", "humidity": "60%"},
    "seoul": {"temperature": "29°C", "conditions": "Humid", "wind_speed": "7km/h", "humidity": "75%"},
    "kuala Lumpur": {"temperature": "31°C", "conditions": "Thunderstorms", "wind_speed": "5km/h", "humidity": "85%"},
    "hanoi": {"temperature": "28°C", "conditions": "Overcast", "wind_speed": "6km/h", "humidity": "80%"},
    "athens": {"temperature": "27°C", "conditions": "Sunny", "wind_speed": "13km/h", "humidity": "45%"},
    "oslo": {"temperature": "16°C", "conditions": "Partly Cloudy", "wind_speed": "14km/h", "humidity": "65%"},
    "vienna": {"temperature": "20°C", "conditions": "Rainy", "wind_speed": "8km/h", "humidity": "75%"},
    "stockholm": {"temperature": "14°C", "conditions": "Chilly", "wind_speed": "12km/h", "humidity": "70%"},
    "abuja": {"temperature": "30°C", "conditions": "Humid", "wind_speed": "9km/h", "humidity": "75%"},
    "dhaka": {"temperature": "33°C", "conditions": "Humid", "wind_speed": "5km/h", "humidity": "85%"},
    "warsaw": {"temperature": "18°C", "conditions": "Cloudy", "wind_speed": "10km/h", "humidity": "70%"},
    "copenhagen": {"temperature": "17°C", "conditions": "Rainy", "wind_speed": "15km/h", "humidity": "80%"},
    "wellington": {"temperature": "13°C", "conditions": "Windy", "wind_speed": "25km/h", "humidity": "70%"},
    "tehran": {"temperature": "36°C", "conditions": "Hot", "wind_speed": "6km/h", "humidity": "30%"},
    "baghdad": {"temperature": "38°C", "conditions": "Very Hot", "wind_speed": "12km/h", "humidity": "25%"},
    "buenos Aires": {"temperature": "16°C", "conditions": "Clear", "wind_speed": "5km/h", "humidity": "60%"},
    "brussels": {"temperature": "19°C", "conditions": "Overcast", "wind_speed": "11km/h", "humidity": "65%"},
    "amman": {"temperature": "29°C", "conditions": "Sunny", "wind_speed": "10km/h", "humidity": "40%"},
    "bucharest": {"temperature": "22°C", "conditions": "Partly Cloudy", "wind_speed": "7km/h", "humidity": "55%"}
}
while True:
    print("\nWeather App Menu")
    print("1. View Weather")
    print("2. Add a City")
    print("3. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        print("\nWelcome to the Weather App.")
        chosen_location = input("What city do you need the weather for?").strip().lower()
        if chosen_location in weather_data:
            weather = weather_data[chosen_location]
            print(f"Weather in {chosen_location.capitalize()}:")
            print(f"Temperature: {weather['temperature']}")
            print(f"Conditions: {weather['conditions']}")
            print(f"Wind Speed: {weather['wind_speed']}")
            print(f"Humidity: {weather['humidity']}")
        else:
            print(f"Sorry, we don't have weather data for {chosen_location}.")
            if chosen_location not in weather_data:
                print(f"City not found. Do you want to add {chosen_location} to the weather app? (yes/no)")
                answer = input().lower()
            
                if answer == "yes":
                    temp = input(f"Enter the temperature for {chosen_location}: ")
                    conditions = input(f"Enter the conditions for {chosen_location}: ")
                    wind_speed = input(f"Enter the wind speed for {chosen_location}: ")
                    humidity = input(f"Enter the humidity for {chosen_location}: ")
                
            
                    weather_data[chosen_location] = {
                        "temperature": temp,
                        "conditions": conditions,
                        "wind_speed": wind_speed,
                        "humidity": humidity
                }
                
                print(f"{chosen_location.capitalize()} has been added to the database!")
            
            elif answer == "no":
                print(f"{chosen_location.capitalize()} is not a valid location at this current point in time.")
            
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")
    if choice == "2":
        new_city = input("Enter the city you want to add: ").strip().lower()
        
        if new_city not in weather_data:
            print(f"This city can be added. Do you want to add {new_city.capitalize()} to the weather app? (yes/no)")
            answer = input().lower()
            
            if answer == "yes":
                temp = input(f"Enter the temperature for {new_city.capitalize()}: ")
                conditions = input(f"Enter the conditions for {new_city.capitalize()}: ")
                wind_speed = input(f"Enter the wind speed for {new_city.capitalize()}: ")
                humidity = input(f"Enter the humidity for {new_city.capitalize()}: ")
                
                weather_data[new_city] = {
                    "temperature": temp,
                    "conditions": conditions,
                    "wind_speed": wind_speed,
                    "humidity": humidity
                }
                
                print(f"{new_city.capitalize()} has been added to the database!")

    if choice == "3":
        print("Exiting the weather app")
        break
    else:
        print("Invalid Option. Please choose 1,2 or 3.")