a = float(input("What is the first number you would like to input?"))
b = float(input("What is the second number you would like to input?"))
operator = input("What operator would you like to use?")
print("add, subtract, multiply, divide, exponentation")

if operator == "add":
  print(a=b)
elif operator == "subtract":
  print(a-b)
elif operator == "multiply":
  print(a*b)
elif operator == "divide":
  print(a/b)
elif operator == "exponentation":
  print(a**b)
else:
  print("Sorry, I do not know that function.")
