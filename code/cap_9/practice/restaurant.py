class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print('restaurant_name: ' + self.restaurant_name + ", cuisine_type: " + self.cuisine_type)

    def open_restaurant_name(self):
        print(self.restaurant_name + ' is open ...')

    def set_number_served(self, number:int):
        self.number_served = number

    def increment_number_served(self):
        self.number_served += 1


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def add_flavors(self, *flavors):
        for flavor in flavors:
            self.flavors.append(flavor)

    def show_flavors(self):
        print('店名：' + self.restaurant_name + ', 口味：' + str(self.flavors))