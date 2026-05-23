#Week 3 Challenge 2
cloud_cover = input("Is the weather Clear or Partly Cloudy?  ")
weather = input("Is it raining or snowing?  ")
temperature = int(input("What is the temperature?  "))
wind_speed = int(input("What is the Wind Speed?  "))
cloud_cover_approved = False
weather_approved = False
temperature_approved = False
wind_speed_approved = False
decision_check = True
while decision_check:
    if cloud_cover == "Clear" or "Partly Cloudy":
        cloud_cover_approved = True
    if weather != "raining" or "snowing":
        weather_approved = True
    if temperature >= 50:
        if temperature <= 85:
            temperature_approved = True
    if wind_speed <= 20:
        wind_speed_approved = True
    if cloud_cover_approved and weather_approved and temperature_approved and wind_speed_approved:
        print("It is a great day to go out and touch some grass!")
        decision_check = False
        break
    else:
        print("It's probably a good day to stay inside and read a book.")
        decision_check = False
        break