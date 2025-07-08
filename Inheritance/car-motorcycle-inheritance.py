class Vehicle:
    def __init__(self,name):
     self.name=name

class Car(Vehicle):
   def __init__(self,name,model,year):
      super().__init__(name)
      self.model=model
      self.year=year 

   def display_info(self):
        print(f"Car name : {self.name},Mode : {self.model}, Year : {self.year}")
class Motorcycle(Vehicle):
   def __init__(self,name,model,year):
      super().__init__(name)
      self.model=model
      self.year=year 
   def display_info(self):
       print(f"Motorcycle name : {self.name},Model : {self.model}, Year : {self.year}")

car = Car("Toyota", "Corolla", 2023)
car.display_info()

motorcycle = Motorcycle("Harley-Davidson", "Street 750", 2020)
motorcycle.display_info()

