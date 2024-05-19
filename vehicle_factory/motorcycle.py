from vehicle_factory.factory import Factory

class Motorcycle(Factory):
    count = 0
    def __init__(self, model, fuel, nw=2):
        super().__init__(model, fuel)
        self._number_of_wheels = nw
        Motorcycle.count += 1

    def get_number_of_wheels(self):
        return self._number_of_wheels

    # def get_count():
    #     return Motorcycle.count
    
    def __str__(self):
        return f"- - - - -\nModel Name: {self._model_name}\nFuel Type: {self._fuel_type}\nNumber of Wheels: {self._number_of_wheels}\n- - - - -"

