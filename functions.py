grades = [2, 5.8, 9, 4.2, 7.1, 3]

def average(mylist):
    the_average = sum(mylist) / len(mylist)
    return the_average


print(average(grades))


# infinite number of arguments
def average(*args):
    return sum(*args) /len(args)

# 
def sum(*args):
    return sum(*args)

# 
def sort_capitalize_str_tupple(*args):
    new_list = [item.upper() for item in args]
    return sorted(new_list)

# 
def find_max(*args):
    return max(args)
print(find_max(3, 99, 1001, 2, 8))



# keyword arguments
def average(**kwargs):
    return kwargs

print(average(a=1, b=2, c=3)) #a dictionary {'a': 1, 'b': 2, 'c': 3}


# 
def find_sum(**kwargs):
    return sum(kwargs.values())
    
print(find_sum(a=3, b=6))


#
def find_winner(**kwargs):
    return max(kwargs, key = kwargs.get)
 
print(find_winner(Andy = 17, Marry = 19, Sim = 45, Kae = 34)) #Sim



# More arguments (definite number)
def area (a, b):
    return a * b

print(area(4, 5))

# 
def concat(a, b):
    return str(a+b)


#Keyword arguments 
def area (a, b):
    return a * b

print(area(b=4, a=5))


# default parameters
def area (a = 2, b = 10):
    return a * b

print(area(6)) #60
print(area(6, 4)) #24
print(area(a=2)) #20


# 
def converter(feet, coefficient = 3.2808):
    meters = feet / coefficient
    return meters
 
print(converter(10)) #3.0480370641306997


# 
def volume(a, b, c):
    return a * b * c
 
print(volume(1, b=2, c=10))