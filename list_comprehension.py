temps = [221, 234, 340, -9999, 230]

# List Comprehension
[i*2 for i in [1, 5, 10]] #[2, 10, 20]
[i*2 for i in [1, -2, 10] if i>0] #[2, 20]
[i*2 if i>0 else 0 for i in [1, -2, 10]] #[2, 0, 20]

# normal loop
new_temps = [temp /10 for temp in temps]

# if
new_temps2 = [temp /10 for temp in temps if temp != -9999]

#if else
new_temps3 = [temp /10 if temp != -9999 else 0 for temp in temps]

print(new_temps)
print(new_temps2)
print(new_temps3)

# 
def sort_values(my_list):
    new_list = [item for item in my_list if isinstance(item, int)]
    return new_list
  
  
# 
def positive_numbers(my_list):
    new_list = [item for item in my_list if item > 0]
    return new_list
  
  
# 
def sort(my_list):
    new_list = [item if isinstance(item, int) else 0 for item in my_list]
    return new_list
  

# 
def convert_sum(my_list):
    new_list = [float(item) for item in my_list]
    list_sum = sum(new_list)
    return list_sum