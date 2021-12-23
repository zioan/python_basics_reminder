username = ''
count = 0

while username != "py":
  username = input("Enter username: ")
  count += 1
  if count == 5:
    print("Too many atemps !")
    break

# 
while True:
  username = input("Enter username2: ")
  if username == "pypy":
      break
  else:
      continue