class bike(object):
    def __init__(self, name, price, max_speed):
        self.name = name
        self.price= price
        self.max_speed = max_speed
        self.miles=0
    def displayinfo(self):
        print "This {}'s price is {} and total miles of {}. It has a max speed of {}.".format(self.name,self.price,self.miles,self.max_speed)
        return self
    def ride(self):
        self.miles += 10
        print "it has been ridden {} miles.".format(self.miles)
        return self
    def reverse(self):
        if self.miles > 5:
            self.miles -= 5
        print "it has been ridden {} miles.".format(self.miles)
        return self

Trek_Emonda=bike("Trek Emonda","$1400","36mph")
Felt_FX4 = bike("Felt FX4","$1195","31mph")
Raleigh_Roper = bike("Raleigh Roper", "$995","26mph")


Trek_Emonda.ride().ride().ride().displayinfo()
Felt_FX4.ride().ride().reverse().reverse().displayinfo()
Raleigh_Roper.reverse().reverse().reverse().displayinfo()
