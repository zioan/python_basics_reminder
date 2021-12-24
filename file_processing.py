### 
# r -read 
# w -write(create file/overwrite !!!) 
# a -open for writing and append at the end. Can't read file !!!
# a+ -open, append and read
# x - create a new file IF the file does not exist and open for writing
# seek(0) - put the cursor at begining of the file

myfile = open('./files/fruits.txt')
file = myfile.read()
myfile.close()
# print(myfile.read())

# or

# no need to close the file, "with" method close it implicitly
with open("./files/fruits.txt") as myfile:
    content = myfile.read()

print(content)





# read
#with open("./files/fruits.txt") as myfile:
# or
#with open("./files/fruits.txt", "r") as myfile:

#write
#if the file/content exists python will overwrite
with open("./files/vegetables.txt", "w") as myfile:
    myfile.write("Tomato\nCucumber\nOnion\n")
    myfile.write("Garlic\n")
    
with open("./files/vegetables.txt", "a+") as myfile:
    myfile.write("\nOkra\n")
    # put the cursot at the begining so the entire file is readed
    myfile.seek(0)
    content2 = myfile.read()
    
print(content2)
    

#print(type(file)) #str

# print first 10 characters
with open("./files/fruits.txt") as content:
    print(content.read(10))
    
# read a file, extract data and write to another file
with open("./files/fruits.txt") as content:
    part_content = content.read(20)
    with open("./files/test.txt", "w") as second_content:
        second_content.write(part_content)
    
#count a character in a file
def foo(character, filepath="./files/fruits.txt"):
    file = open(filepath)
    content = file.read()
    return content.count(character)