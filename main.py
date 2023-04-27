from datetime import date as dt


class Employee:
   def __init__(self, name, age):
      self.name = name
      self.age = age
      
   def isAdult(self, age):
      if age > 18:
         return True
      else:
         return False
     
   @classmethod
   def emp_from_year(cls, name, year):
      return cls(name, dt.today().year - year)
  
  
   def __str__(self):
      return 'Employee Name: {} and Age: {}'.format(self.name, self.age)
  
  
  
e1 = Employee('Dhiman', 25)
print(e1)
e2 = Employee.emp_from_year('Subhas', 1987)
print(e2)
print(Employee.isAdult())
print(Employee.isAdult())