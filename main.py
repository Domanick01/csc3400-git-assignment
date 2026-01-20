import calculator

num1 = int(input("What is the first number you want to add?\n"))
operator = input("What operator would you like to use (+,-,*,/)\n")
num2 = int(input("What is the second number you want to add?\n"))

print("Result:")

if operator == "+":
   calculator.add(num1, num2)
elif operator == "-":
   calculator.subtract(num1, num2)
elif operator == "*":
   calculator.multiply(num1, num2)
elif operator == "/":
   calculator.divide(num1,num2)
elif operator == "pow":
   calculator.pow(num1, num2)
elif operator == "sqrt":
   calculator.square_root(num1, num2)