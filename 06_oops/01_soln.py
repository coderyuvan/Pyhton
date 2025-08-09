class Car:
    # constructor maded and self = this of javascript

    total_car=0
    def __init__(self,brand,model):
        # __ Private mark krdia h attribute ko
        self.__brand = brand
        self.__model = model
        Car.total_car+=1
    
    # getter
    def get_brand(self):
        return self.__brand + " ->>>>>"
    
    def show_details(self):
        print(f"the name of car is {self.__brand} and model is {self.__model}")

    # static method
    @staticmethod
    def general_description():
        print("This is a general description of the car class.") 

   # decorators
    
    @property
    def model(self):
        return self.__model
        

class Electric_car(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size=battery_size
    
    # def show_details(self):
    #     print(f"the name of car is {self.brand} and model is {self.model} and size of battery is {self.battery_size}")

#my_ev=Electric_car("tata","safari","5000p")
my_car=Car("TESLA","tesla-S")
# can't be dne operation
my_car.model="Model X"
print("Total Number of Cars : ",Car.total_car)
# marked as private using __
#print(my_car.__brand)
print(my_car.get_brand())
# print(my_ev.battery_size)
# print(my_ev.brand)
# print(my_ev.model) 
#print(my_ev.show_details())

print(Car.general_description())
print(my_car.model)  