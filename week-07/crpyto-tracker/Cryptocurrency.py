import requests
import time

class Cryptocurrency:
    def __init__(self,name,symbol):
        self.name = name
        self.symbol = symbol
        self.users = []
    def add_user(self,user):
        self.users.append(user)
        
    def notify(self,crypto_price):
        for user in self.users:
            user.update(crypto_price,self.name)
    def monitor_price(self,interval):
        while True:
            url = f"https://api.coingecko.com/api/v3/simple/price?ids={self.symbol}&vs_currencies=usd"
            response = requests.get(url,timeout=60)
            coin = response.json()
            price = coin[self.symbol]["usd"]
            self.notify(price)
            time.sleep(interval)