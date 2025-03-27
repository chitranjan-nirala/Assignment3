# Problem Statement: Write a Python program that:
# 1.   Asks the user for a number as input.
# 2.   Uses the math module to calculate the:
# o   Square root of the number
# o   Natural logarithm (log base e) of the number
# o   Sine of the number (in radians)
# 3.   Displays the calculated results.

num = int(input("enter any nnumber: "))
import  math
res = math.sqrt(num)
res1 = math.log(num)
res2= math.sin(num)
print(f"saquaroot of {num} is {res}")
print(f"saquaroot of {num} is {res1}")
print(f"saquaroot of {num} is {res2}")