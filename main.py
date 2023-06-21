# Create a class of person with multiple properties
# Generate a person with all properties
# Create a function that uses 3 properties from the person, and creates an email address

class AdvancedPerson:
  def __init__(self, firstName, lastName, age, areaCode, city, birthYear, zipCode, favEmail):
    self.firstName = firstName
    self.lastName = lastName
    self.age = age
    self.areaCode = areaCode
    self.city = city
    self.birthYear = birthYear
    self.zipCode = zipCode
    self.favEmail = favEmail

robert = AdvancedPerson("Robert", "Doe", "68", "423", "Chattanooga", "1954", "37403", "hotmail")

christopher = AdvancedPerson("Christopher", "Barnes", "67", "510", "Commerce", "1956", "90040", "hotmail")

femi = AdvancedPerson("Femi", "Oluwaleye", "31", "651", "StPaul", "1991", "11212", "gmail")


def emailGenerator(val1, val2, val3, favEmail):
  email = val1 + val2 + val3 + "@" + favEmail + ".com"
  return email

print(emailGenerator(femi.firstName, femi.zipCode, femi.birthYear, femi.favEmail))

#def emailGenerator(
#val1 = femi.firstName
#femi.firstName = "Femi"

#val2 = femi.zipCode
#femi.zipCode = 11212

#val3 = femi.birthYear
#femi.birthYear = 1991

#favEmail = femi.favEmail
#femi.favEmail = gmail

#email = val1 + val2 + val3 + "@" + favEmail + ".com"

#email = Femi112121991@gmail.com





