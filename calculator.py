num1 = int(input("What is the first number you want to add?\n"))
operator = input("What operator would you like to use (+,-,*,/)\n")
num2 = int(input("What is the second number you want to add?\n"))

print("Result:")

if operator == "+":
   print(num1 + num2)
if operator == "-":
   print(num1 - num2) 
if operator == "*":
   print(num1 * num2)
if operator == "/":
   print(num1/num2)
