class ConcreteUser:
    def __init__(self,name,buy_threshold,sell_threshold):
        self.name = name
        self.buy_threshold = buy_threshold
        self.sell_threshold = sell_threshold
    
    def update(self,crypto_price,coin_name):
        print(f"{self.name} received update: {coin_name} is now ${crypto_price}")
        if (crypto_price< self.buy_threshold):
            print(f"{self.name} : It's time to Buy {coin_name}!")
        elif(crypto_price> self.sell_threshold):
            print(f"{self.name} : It's time to SELL {coin_name}!")