# Write a program to print the multiplication table of a number in the format 5X1=5, 5X2=10.

number = int(input("Enter number : "))

for i in range(1, 11):
    print(f"{number} X {i} = {number*i}")