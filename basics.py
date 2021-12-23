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