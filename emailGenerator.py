def emailGenerator(arg1, arg2, arg3, favEmail):
  print(arg1+arg2+arg3 +"@"+favEmail+".com")

class AdvancedPerson:
  def __init__(self, firstName, lastName, age, areaCode, city, birthYear, zipCode, favEmail):
    self.firstName = firstName
    self.lastName = lastName
    self.age = age
    self.areaCode = areaCode
    self.city = city
    self.birthYear = birthYear
    self.favEmail = favEmail
    self.zipCode = zipCode

femi = AdvancedPerson("Femi", "Oluwaleye", 31, 651, "StPaul", "1991", "11212" "gmail")

emailGenerator()