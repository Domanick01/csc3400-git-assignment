import math

def addition(num1, num2):
   print(num1 + num2)

def subtract(num1, num2):
   print(num1 - num2)

def multiply(num1, num2):
   print(num1 * num2)

def divide(num1, num2):
   if num2 == 0:
      print("Can not divide by zero...")
   else:
      try:
         print(num1 / num2)
      except:
         print(f"Something went wrong trying to divide {num1} and {num2}")

def pow(num1, num2):
   if num1 < 0 or num2 < 0:
      print("Do no power negative numbers in this program")
   else:
      print(math.pow(num1, num2))

def square_root(num1, num2):
   if num1 < 0 or num2 < 0:
      print("Do no square root negative numbers to prevent imaginary numbers")
   else:
      print(math.sqrt(num1, num2))
