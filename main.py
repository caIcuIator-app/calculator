import time
import replit
import math
import factorial
# This is the function for the subtraction part.
def subtraction():
  print("Enter two numbers separately.")
  number1 = float(input("Your minuend... "))
  number2 = float(input("Your subtrahend... "))
  print(f"Your difference is {number1 - number2}.")
#This part is the beginning of the script run
print("What math function would you like to do?")
time.sleep(5.4302745)
replit.clear()
print("1 = Addition")
print("2 = Subtraction")
print("3 = Multiplication") 
print("4 = Full Division")
print("5 = Square Root")
print("6 = Digits of Pi")
print("7 = Exponents")
print("8 = Factorial Calculator")
print("9 = Division with Remainders Left Over")
print("10 = Cube Root")
func = int(input(""))
if func == 6:
  replit.clear()
  print("The value of pi is:")
  time.sleep(1.1)
  replit.clear()
  print(math.pi)
elif func==10:
    replit.clear()
    print("Enter a number. If you want the cube root of pi, just enter 'math.pi'.")
    cuberootraw = input("")
    if cuberootraw == "math.pi":
      replit.clear()
      print(f"The cube root of pi is {(math.pi)**(1/3)}.")
    else:
      cuberoot = float(cuberootraw)
      replit.clear()
      print(f"The cube root of your number is {cuberoot**(1/3)}.") #Don't use a string other than 'math.pi' or you'll break the calculator.
elif func == 1:
  replit.clear()
  print("Enter the first number.")
  num1 = int(input(""))
  num2 = int(input("Enter the second number... "))
  print("Your answer is...")
  print(num1+num2)
elif func == 2:
  replit.clear()
  subtraction()
elif func == 5:
    replit.clear()
    print("Enter a number. If you want the square root of pi, just enter 'math.pi'.")
    squarerootraw = input("")
    if squarerootraw == "math.pi":
      replit.clear()
      print(f"The positive square root of pi is {math.sqrt(math.pi)}.")
    else:
      squareroot = float(squarerootraw)
      replit.clear()
      print(f"The square root of your number is {math.sqrt(squareroot)}.")

elif func == 3:
  replit.clear()
  print("Enter two numbers separately.")
  factor1 = int(input(""))
  factor2 = int(input(""))
  print("The product of the numbers is...")
  time.sleep(2.14)
  replit.clear()
  print(factor2 * factor1)
elif func == 4:
  replit.clear()
  print("Enter 2 numbers separately.")
  dividend = int(input("Your dividend... "))
  divisor = int(input("Your divisor... "))
  print("Your quotient is...")
  time.sleep(2.41)
  replit.clear()
  print(dividend / divisor)
elif func == 7:
  replit.clear()
  print("Enter your base.")
  base = int(input(""))
  print("Enter the exponent your base is raised to.")
  exponent = int(input(""))
  if exponent == 0:
    print("Your base raised to your exponent is 1.")
  else:
    print("Your base raised to your exponent is...")
    time.sleep(2.14253925017303628193687264826)
    print(base**exponent) 
elif func == 8:
  factorial.factorial()
elif func == 9:
  replit.clear()
  div = float(input("Your dividend..."))
  divisor = float(input("Your divisor..."))
  quotient = div//divisor # rounds the quotient down.
  print(f"----\nThe quotient is {quotient}.")
else:
  replit.clear()
  print("That number was not an option.")
  print("Run the script again.")
