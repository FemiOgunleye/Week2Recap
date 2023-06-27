def emailGenerator(arg1, arg2, arg3, favEmail):
  print(str(arg1)+str(arg2)+str(arg3) +"@"+str(favEmail)+".com")

class NextLevelPerson:
  def __init__(self, firstName, lastName, age, areaCode, city, birthYear, zipCode, favEmail):
    self.firstName = firstName
    self.lastName = lastName
    self.age = age
    self.areaCode = areaCode
    self.city = city
    self.birthYear = birthYear
    self.zipCode = zipCode
    self.favEmail = favEmail




firstNameUser = input("Enter your first name: ")
lastNameUser = input("Enter your last name: ")
ageUser = int(input("Enter your age: "))
areaCodeUser = int(input("Enter your area code: "))
cityUser = input("Enter your city: ")
birthYearUser = int(input("Enter your birth year: "))
favEmailUser = input("Enter your favorite email company: ")
zipCodeUser = input("Enter your zip code: ")


user = NextLevelPerson(firstNameUser, lastNameUser, ageUser, areaCodeUser, cityUser, birthYearUser, zipCodeUser, favEmailUser)

emailGenerator(user.firstName, user.city, user.birthYear, user.favEmail)
