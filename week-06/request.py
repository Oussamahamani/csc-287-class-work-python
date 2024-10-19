import requests
import sys


if(len(sys.argv)!=1):
    city_name = sys.argv[1]
    url = f"https://wttr.in/{city_name}?format=j1"
    response = requests.get(url,timeout=60)
    weather = response.json()
    print(weather["weather"][0]["astronomy"][0]["sunset"])
else:
    print("you need to pass an argument")

