#check if the given number is integer, odd/even/0 and return a dictionary

def foo(x):
  result = {"sign":"", "parity":""}
  if x == 0 :
      result["parity"] = 'even'
      result["sign"] = 'zero'
  elif isinstance(x, float) :
      result["parity"] = 'not integer'
      if x > 0 :
        result["sign"] = 'positive'
      else:
        result["sign"] = 'negative'      
  elif x > 0 :
      result["sign"] = 'positive'
      if x % 2 == 0:
          result["parity"] = 'even'
      else:
          result["parity"] = 'odd'
  else: #x < 0 
      result["sign"] = 'negative'
      if x % 2 == 0:
          result["parity"] = 'even'
      else:
          result["parity"] = 'odd'
  return result
      
      
print(foo(-6.1))
