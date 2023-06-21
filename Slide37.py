#print("Hello world, welcome to Python!")




# function with two arguments
def add_numbers(num1, num2):
    sum = num1 + num2
    print('Sum: ',sum)

# function call with two values



thislist = ["apple", "banana", "cherry", "mango"]


score = 44
if score > 100:
   print ("Woah! Really high marks for you!")
   print (score)
elif score > 90:
   print ("Great job! You did excellent on the exam!")
   print (score)
elif score > 80:
   print ("Good job! You passed the exam!")
   print (score)
elif score > 70:
 print ("At least you passed the exam!")
 print (score)
else:
   print ("Do us and yourself a favor, take a week before taking the exam again, kthanks")
   print (score)

print ("Good bye!")



6/20 Lesson 1



























firstName = "Femi"
lastName = "Oluwaleye"
age = 31

#print("Next year's age equals: ", age + 1, type(age))
#print("First name equals: ", firstName, type(firstName))
#print("Last name equals: ", lastName, type(lastName))

class Person:
  firstName = "Femi"
  lastName = "Oluwaleye"
  age = 31
  phone = 1231231234
  absent = False
  city = "Princeton"




femiO = Person()
#print(femiO.lastName)


class AdvancedPerson:
  def __init__(self, firstName, lastName, age, phone, absent, city, birthday):
    self.firstName = firstName
    self.lastName = lastName
    self.age = age
    self.phone = phone
    self.absent = absent
    self.city = city
    self.birthday = birthday

femiOl = AdvancedPerson("Femi", "Oluwaleye", 31, 1231231234, False, "Princeton", "07/03/1991")
#print(femiOl.city)
derrickJ = AdvancedPerson("Derrick", "Jarrett", 59, 9256655007, False, "Oakland", "08/07/1963")
#print(derrickJ.birthday)



count = 0
while (count < 5):
  count = count + 1
  #print("Count = ", count)

x = 3
for num in range(0,x):
  print(num)
  
