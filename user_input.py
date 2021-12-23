# x = int(input("Enter a temperature: "))
x=3

def temp(x):
  if x > 7:
    return "Warm"
  else:
    return "Cold"

print(temp(x))


# String formating expresion

name = "Sim"
experience_years = 1.5
print("Hi %s, you have %s years of experience." % (name, experience_years))

name = "Sim"
experience_years = 1.5
print("Hi {}, you have {} years of experience".format(name, experience_years))


# user_input = input("Enter your name: ")
name = input("Enter your name: ").title()
surname = input("Enter your surname: ").title()
when = "today"
# works in python 2 and 3
message = "Hello %s" % name
message2 = "Hello %s %s" % (name, surname)
#from python 3.6 +
message = f"Hello there {name}!"
message2 = f"Hello there {name} {surname}! What's up {when}"
print(message)
print(message2)

