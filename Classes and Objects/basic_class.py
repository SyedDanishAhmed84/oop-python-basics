class Person:
    def __init__(self):
        self.name=" Syed Danish Ahmed"
        self.age=20
        self.domain="Engineering"
        self.email="daniahmed755@gmail.com"
        self.Github="https://github.com/SyedDanishAhmed84"
        self.LinkedIn="https://www.linkedin.com/in/syed-danish-ahmed-91a9a22b6/"
    def display(self):
     print(f"Name : {self.name}")
     print(f"Age : {self.age}")
     print(f"Domain : {self.domain}")
     print(f"Email : {self.email}")
     print(f"Github : {self.Github}")
     print(f"LinkedIn : {self.LinkedIn}")
p1=Person()
p1.display()