class Student:
    def __init__(self):
        self .__name=None
        self .__age=None
        self .__city=None
        self .__marks=None

    def set_name(self,name):
        self .__name=name
    def set_age(self,age):
        self .__age=age    
    def set_city(self,city):
        self .__city=city
    def set_marks(self,marks):
        self .__marks=marks

    def get_name(self):
        return self .__name
    def get_age(self):
        return self .__age
    def get_city(self):
        return self .__city
    def get_marks(self):
        return self .__marks
    def calculate_grade(self):
        if self .__marks >= 85:
            return "A"
        elif self .__marks >=70 and self .__marks<85:
            return "B"
        elif self .__marks >=60 and self .__marks<70:
            return "C"
        elif self .__marks >=50 and self .__marks<60:
            return "D"
        elif self .__marks<50:
            return "F"
        else:
            return "Invalid"
        
    def display_info(self):
        print(f"Name : {self .__name}")
        print(f"Age : {self .__age}")
        print(f"City : {self .__city}")
        print(f"Marks : {self .__marks}")
        print(f"Grade : {self.calculate_grade()}")
        
    
s1=Student()
s1.set_name("Syed Danish Ahmed") 
s1.set_age(20)   
s1.set_city("Karachi")
s1.set_marks(95)
s1.display_info()
