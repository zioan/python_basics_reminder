temps = [9.1, 8.8, 7.6, 4.5, 5.3]

for temp in temps:
    print(round(temp))
    print("Done")

for letter in "hello !":
    # print(letter)
    print(letter.title())


#
for i in [1, 2, 3, "abc", True]:
  print(i)

# 
def celsius_to_kelvin(cels):
    return cels + 273.15

monday_temperatures = [9.1, 8.8, -270.15]
 
for temperature in monday_temperatures:
    print(celsius_to_kelvin(temperature))


# dictionary
student_grades = {"Marry": 9.1, "Bob": 8.8, "John": 7.5}

for items in student_grades.items():
  print(items)

for names in student_grades.keys():
  print(names)

for grades in student_grades.values():
  print(grades)


# 
phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
 
for pair in phone_numbers.items():
    print("{} has as phone number {}".format(pair[0], pair[1]))
# John Smith has as phone number +37682929928
# Marry Simpons has as phone number +423998200919


# 
for key, value in phone_numbers.items():
    print("{} has as phone number {}".format(key, value))
# John Smith has as phone number +37682929928
# Marry Simpons has as phone number +423998200919
