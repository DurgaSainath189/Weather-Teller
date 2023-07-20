import requests
import json
import pyttsx3

city_name = input("Enter the name of the city: ")
response = f"https://api.weatherapi.com/v1/current.json?key=c7dcca126aa74fe785a52745232007&q={city_name}"
result = requests.get(response)
data = json.loads(result.text)
temperature = data["current"]["temp_c"]
date_and_time = data["location"]["localtime"]
print(f"The Temperature in {city_name} is {temperature} degrees celcius and the local data and time is {date_and_time}")
start = pyttsx3.init()
start.say(f"The Temperature in {city_name} is {temperature} degrees celcius and the local data and time is {date_and_time}")
start.runAndWait()
