grades = [2, 5.8, 9, 4.2, 7.1, 3]
students_grades = {"Marry": 9.1, "Sim": 8.8, "John": 7.5}

def average(object):
    if isinstance(object, dict):
    # if type(object) == dict:
        the_average = sum(object.values()) / len(object)
    # elif ...
    else:
        the_average = sum(object) / len(object)
    return the_average


print(average(grades))
print(average(students_grades))


# 
x = 1
 
if x == 1:
    print("Yes")
else:
    print("No")


# and
x = 1
y = 1
 
if x == 1 and y == 1:
    print("Yes")
else:
    print("No")


# or
x = 1
y = 1
 
if x == 1 or y == 2:
    print("Yes")
else:
    print("No")

# 
message = "hello there"
 
if "hello" in message:
    print("hi")
else:
    print("I don't understand")

# 
message = "hello there"
 
if "hello" in message:
    print("hi")
elif "hi" in message:
    print("hi")
elif "hey" in message:
    print("hi")
else:
    print("I don't understand")


# Check if a value is of a particular type with:

isinstance("abc", str)
isinstance([1, 2, 3], list)

# or

type("abc") == str
type([1, 2, 3]) == list
