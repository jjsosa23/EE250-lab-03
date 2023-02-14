import requests
from typing import Dict
import json

# connect to a "real" API

## Example: OpenWeatherMap
URL = "https://api.openweathermap.org/data/2.5/weather"

# TODO: get an API key from openweathermap.org and fill it in here!
API_KEY = "8715b47444aac521719209e8fd505b07"

def get_weather(city) -> Dict:
    res = requests.get(URL, params={"q": city, "appid": API_KEY})
    return res.json()

# TODO: try connecting to a another API! e.g. reddit (https://www.reddit.com/dev/api/)

def get_bitcoin_price() -> Dict:
    res = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json") #connects to coinDesk api
    bitCoinData = res.json()
    price = bitCoinData["bpi"]["USD"]["rate"] #displays current bitcoin price
    print("Current bitcoin price: "+price +"\n")
    return bitCoinData

def main():
    temp = get_weather("London")
    print(temp)
    print("\n\n")
    #get_bitcoin_price()
    print(get_bitcoin_price())

if __name__ == "__main__":
    main()