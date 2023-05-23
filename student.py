from datetime import date
class Student:
    def __init__(self, firstname, lastname, dob, gender) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.dob = dob
        self.gender = gender

    def showself(self):
        print(self)
  
    def fullname(self):
        return f"{self.firstname} {self.lastname}"
   
    def get_age(self):
        return date.today().year - int(self.dob[-4:])
    
sampath = Student("Sampath", "K", "23-05-2001", "M")

naveen = Student

harika = naveen("Harika", "N", "23-05-2001", "F")

priyanka = Student("Priyanka", "P", "23-05-2001", "F")

print(sampath.fullname())
print(harika.fullname())
print(priyanka.fullname())





