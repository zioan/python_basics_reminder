# if list len=3 remove first element and append ojs, else return none
def foo(mylist, obj):
    if len(mylist) == 3:
        newlist = mylist[1:]
        # newlist.pop(0)
        newlist.append(obj)
        return newlist
      
print(foo([1, 2, 3], 'a'))


# every 7 element
def foo(mylist):
    return mylist[::7]
  
