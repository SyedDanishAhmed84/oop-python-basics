class Temperature:
    def __init__(self,temperature):
        self.temperature=temperature
    def to_fehrenheit(self):
        return(self.temperature*9/5)+32 
    def to_celsius(self):
        return(self.temperature-32)*5/9
t1=Temperature(7)
print(f"Temperature in Celsius is : {t1.to_fehrenheit()}")
print(f"Temperature in Celsius is : {t1.to_celsius()}")    
    