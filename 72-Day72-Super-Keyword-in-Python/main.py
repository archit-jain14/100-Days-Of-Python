class Employee:
  def __init__(self, name, id):
    self.name = name
    self.id = id

class Programmer(Employee):
  def __init__(self, name, id, lang):
    super().__init__( name, id)
    self.lang = lang

rohan = Employee("Rohan Das", "420")
Archit = Programmer("Archit", "2345", "Python")
print(Archit.name)
print(Archit.id)
print(Archit.lang)
