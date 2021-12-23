# Variables
day_hours = 24
week_days = 7

week_hours = day_hours * week_days

print(week_hours)

i = 5
s = "10"
f = 2.5

# Lists
# grades = [9.1, 8.8, 7.5]

# list(range(1, 10))
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

# list(range(1, 10, 2))
# [1, 3, 5, 7, 9]

# dir(list)

numbers = [2, 5.8, 9, 4.2, 7.1, 3]

print (len(numbers))

grades = [9.1, 8.8, 7.5]

mean = sum(grades) / len(grades)

print(mean)


# Dictionary - mutable
student_grades = {"Marry": 9.1, "Bob": 8.8, "John": 7.5}

# mean = sum(student_grades.values()) / len(student_grades.keys())
mean = sum(student_grades.values()) / len(student_grades)

print(mean)


students = student_grades.keys()
grades = student_grades.values()

print(students)
print(grades)


# Tupple - tupples are immutable (no append, remove ...)
temperatures = (1, 4, 5)

#Lists, strings, and tuples have a positive index system:
["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
#  0      1      2      3      4      5      6

#And a negative index system:
["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
# -7     -6     -5     -4     -3     -2     -1

# In a list, the 2nd, 3rd, and 4th items can be accessed with:
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
days[1:4]
# Output: ['Tue', 'Wed', 'Thu']

# First three items of a list:
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
days[:3]
# Output:['Mon', 'Tue', 'Wed'] 

# Last three items of a list:
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
days[-3:]
# Output: ['Fri', 'Sat', 'Sun']

# Everything but the last:
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
days[:-1] 
# Output: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'] 

# Everything but the last two:
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
days[:-2] 
# Output: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'] 

# A single in a dictionary can be accessed using its key:
phone_numbers = {"John Smith":"+37682929928","Marry Simpsons":"+423998200919"}
phone_numbers["Marry Simpsons"]
# Output: '+423998200919'

# DATATYPES CONVERTION
# From tuple to list:
# >>> data = (1, 2, 3)
# >>> list(data)
# [1, 2, 3]

# From list to tuple:
# >>> data = [1, 2, 3]
# >>> tuple(data)
# (1, 2, 3)

# From list to dictionary:
# >>> data = [["name", "John"], ["surname", "smith"]]
# >>> dict(data)
# {'name': 'John', 'surname': 'smith'}

