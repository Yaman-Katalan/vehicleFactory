class Factory:
    count = 0
    def __init__(self, model, fuel):
        self._model_name = model
        self._fuel_type = fuel
        Factory.count += 1

    def get_model(self):
        return self._model_name
    
    def get_fuel(self):
        return self._fuel_type

    def change_model(self, changed_model):
        self._model_name = changed_model
        return "model successfully changed!"
    
    def change_fuel(self, changed_fuel):
        if changed_fuel == "electric" or changed_fuel == "petrol" or changed_fuel == "diesel":
            self._fuel_type = changed_fuel
            return "Fuel changed successfully"
        else:
            return "No such fuel. Please enter a valid value."

    @classmethod
    def get_count(cls):
        return cls.count

    def __str__(self):
        return "Hello Factory!"

# print(Factory.get_count())