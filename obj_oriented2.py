class Students:
  name = "Imran"
  grade = 2
  def intro(self):
    print("Hi,I am a student")
  def details(self):
    print("My name is",self.name)  
    print("I study in grade",self.grade)

obj = Students()
obj.intro()  
obj.details()