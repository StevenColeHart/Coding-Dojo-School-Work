class Product(object):
    def __init__(self,price,item_name,weight,brand):
        self.price=price
        self.item_name = item_name
        self.weight=weight
        self.brand=brand
        self.status="for sale"
    def sold(self):
        self.status="sold"
    def returned(reason):
        if reason = defective:
            print True
            return self

    def tax(self):
        self.taxes = round(( self.price * 1.1025),2)
        return self
    def display_all_info(self):
        self.tax()
        print "Item name:{}".format(self.item_name)
        print "Price:{}".format(self.price)
        print "Price after taxes:{}".format(self.taxes)
        print "Weight:{}".format(self.weight)
        print "Brand:{}".format(self.brand)
        print "Status: {}".format(self.status)
Amazon_Echo=Product(149,"Echo",1.25,"Amazon")

Amazon_Echo.returned(defective).display_all_info()
