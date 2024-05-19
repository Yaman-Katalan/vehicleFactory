from vehicle_factory.factory import Factory

class Car(Factory):
    count = 0
    def __init__(self, model, fuel, color, nd=4):
        super().__init__(model, fuel)
        self._number_of_doors = nd
        self._car_color = color
        Car.count += 1
    
    def get_color(self):
        return self._car_color
    
    def get_number_of_doors(self):
        return self._number_of_doors
    
    def change_number_of_doors(self, changed_number):
        if changed_number == 2 or changed_number == 4:
            self._number_of_doors = changed_number
            return "Successfully changed."
        else:
            return "You can only choose between 2 or 4."
    
    def change_color(self, changed_color):
        self._car_color = changed_color
        return "Color changed successfully."
    
    # def get_count():
    #     return Car.count
    
    def __str__(self):
        return f"- - - - -\nModel Name: {self._model_name}\nFuel Type: {self._fuel_type}\nNumber of Doors: {self._number_of_doors}\nCar Color: {self._car_color}\n- - - - -"


