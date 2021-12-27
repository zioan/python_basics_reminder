#>>> import sys
#>>> sys.builtin_module_names
#import time
#dir(time)
#help(time.sleep)

#standard modules (builtins)
import time
import os
  
# while True:
#   if os.path.exists("./files/vegetables.txt"):
#       with open("./files/vegetables.txt") as file:
#           print(file.read())
#   else:
#       print("file does not exists")
#   time.sleep(60)
  
  
#third-party modules
#pip3.10 install pandas
#import pandas
#dir(pandas)
#help(pands.***)

import pandas

while True:
  if os.path.exists("./files/temps_today.csv"):
      data = pandas.read_csv("./files/temps_today.csv")
      print(data.mean()["st1"])
      # print(data.mean())
  else:
      print("file does not exists")
  time.sleep(3)
  
