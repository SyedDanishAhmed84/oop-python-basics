class Book:
    def __init__(self,title,author,year,writer,prize):
        self.title=title
        self.author=author
        self.year=year
        self.writer=writer
        self.prize=prize
    def display(self):
        print(f"Title : {self.title}")
        print(f"Author : {self.author}")
        print(f"Year : {self.year}")
        print(f"Writer : {self.writer}")
        print(f"Prize : {self.prize}")
book1=Book("Atomic Habits","James Clear",2018,"James Clear",300)
book2=Book("Can't Hurt me","David Goggins",2018,"David Goggins",400)
book3=Book("Rich Dad Poor Dad","Robert Kiyosaki",1997,"Robert Kiyosaki",500)
book1.display()
book2.display()
book3.display()