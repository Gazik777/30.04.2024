import json
import pickle

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def to_json(self):
        return json.dumps({"brand": self.brand, "model": self.model, "year": self.year})

    @staticmethod
    def from_json(json_data):
        data = json.loads(json_data)
        return Car(data["brand"], data["model"], data["year"])

    def to_pickle(self):
        return pickle.dumps(self)

    @staticmethod
    def from_pickle(pickle_data):
        return pickle.loads(pickle_data)


car = Car("Книга", "Наши дни", 1997)


json_data = car.to_json()
print(f"Данные в формате JSON: {json_data}")

new_car_json = Car.from_json(json_data)
print(f"Новый автомобиль из JSON: {new_car_json.brand} {new_car_json.model} ({new_car_json.year})")

pickle_data = car.to_pickle()
print(f"Данные в формате Pickle: {pickle_data}")

new_car_pickle = Car.from_pickle(pickle_data)
print(f"Новый автомобиль из Pickle: {new_car_pickle.brand} {new_car_pickle.model} ({new_car_pickle.year})")