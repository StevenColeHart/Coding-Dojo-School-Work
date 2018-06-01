class Car(object):
    def __init__(self, price, top_speed, fuelmpg, tankrange):
        self.price = price
        self.top_speed = top_speed
        self.fuelmpg = fuelmpg
        self.tankrange = tankrange
        self.taxes = 0
    def tax(self):
        if self.price > 25000:
            self.taxes = "15%"
        elif self.price < 25000:
            self.taxes = "12%"
        return self
    def display_all(self):
        self.tax()
        print "Price: {}".format(self.price)
        print "Top Speed: {}".format(self.top_speed)
        print "Fuel Economy: {}".format(self.fuelmpg)
        print "Max Range: {}".format(self.tankrange)
        print "Tax: {}".format(self.taxes)

Hyundai_Accent = Car(8885,"102mph","38mpg",360)
Nissan_GTR = Car(120000,"180mp","22mpg",280)



Hyundai_Accent.display_all()
Nissan_GTR.display_all()


