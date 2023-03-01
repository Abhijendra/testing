import requests
from datetime import datetime 
import tzlocal 

user_api = "2a43da31fbde7e49d86931bfe9dc118a"
location = input("Enter the location here: ")

complete_api_link = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={user_api}"

api_link = requests.get(complete_api_link)
api_data = api_link.json()

if api_data["cod"]=="404":
    print("Invalid City Name. Please enter it correctly!")
    exit()

temp_in_C = round(api_data["main"]["temp"] - 273)
desc = api_data["weather"][0]["description"]
hmdt = api_data["main"]["humidity"]
wnd_spd = api_data["wind"]["speed"]
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")
lat = api_data["coord"]["lat"]
lon = api_data["coord"]["lon"]
cld_cvr = api_data["clouds"]["all"]
snrs_tm = datetime.fromtimestamp(api_data["sys"]["sunrise"], tzlocal.get_localzone()).strftime("%I:%M:%S %p")
snst_tm = datetime.fromtimestamp(api_data["sys"]["sunset"], tzlocal.get_localzone()).strftime("%I:%M:%S %p")
country = api_data["sys"]["country"]


print('----------------------------------------------------------------------')
print(f"Weather stats for {location.upper()}({lat}, {lon}), {date_time}")
print('----------------------------------------------------------------------')

print(f"Current Temperature is {temp_in_C} deg C")
print("Description:", desc)
print("Humidity: ", hmdt, "%")
print("Wind Speed:", wnd_spd, 'kmph')
print("Cloud Cover:", cld_cvr, "%")
print("Sunrise Time:", snrs_tm)
print("Sunset Time:", snst_tm)
print("Country:", country)