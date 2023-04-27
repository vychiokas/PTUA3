from datetime import date
import datetime

class Person:
    description: str = "A simple normal human being"
    
    def __init__(self, name: str, surname: str):
        self.name: str = name
        self.surname: str = surname
        # print(self.greet())

    def greet(self):
        return f"Hello my name is {self.name}"


    def walk_away(self):
        return f"{self.name} is walking away..."
    
    
    
    def calculate_days_left_till_black_friday(self) -> int:
        # get todays date
        # initialize black friday date
        # return black_friday_date - todays_date
        today = date.today()
        black_friday_date = datetime.date(2023, 11, 24)
        delta = black_friday_date - today
        return delta.days

    
    def get_eye_color(self, eye_color: str = "Brown") -> str:
        return eye_color
    
    def __repr__(self):
        return f"Person: {self.name}-{self.surname}"
    
    def __str__(self):
        return f"P: {self.name}-{self.surname}"

person1 = Person("Vytautas", "Sluckas")
print(person1)
print(repr(person1))
# print(person1.get_eye_color("Blue"))