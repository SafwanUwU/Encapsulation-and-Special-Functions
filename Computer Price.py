class Computer:
    def __init__(self):
      self.__maxprice = 900

    def sell(self):
      print(f"Selling price: {self.__maxprice}")

    def setMaxprice(self, price):
      self.__maxprice = price

c = Computer()
c.sell()

#change the price
c.__maxprice = 1000
c.sell()

#using setter function
c.setMaxprice(1500)
c.sell()