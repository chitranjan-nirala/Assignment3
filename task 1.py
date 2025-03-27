# Problem Statement: Write a Python program that:
# 1.   Defines a function named factorial that takes a number as an argument
# and calculates its factorial using a loop or recursion.
# 2.   Returns the calculated factorial.
# 3.   Calls the function with a sample number and prints the output.
num = int(input("enter any number: "))
def factorial(num):
    fact =1
    for n in range(1,num+1):
        fact = fact * n
    return fact

print(f"factorial of {num} is : {factorial(num)}")

      # using recursion
# def factorial(num):
#     if num ==1 or num==0:
#         return 1
#     return factorial (num-1)* num
# print(f"factorial of {num} is : {factorial(num)}")