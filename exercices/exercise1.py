final_string = ""
questions = ("how", "what", "where", "why")
    

def sentence(phrase):
  capitalized = phrase.capitalize()
  if phrase.startswith(questions):
      # return "{}? ".format(capitalized)
      return capitalized + "? "
  else:
      # return "{}. ".format(capitalized)
      return capitalized + ". "


while True:
  user_input = input("Say something: ")
  if user_input == "end":
      print(final_string)
      break
  else:
      final_string += sentence(user_input)