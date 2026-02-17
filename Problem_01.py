# Write a program to swap two numbers without using a third variable

num1 = 5
num2 = 10

print(f"Before Swapping : {num1, num2}")

num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2

print(f"After Swapping : {num1, num2}")