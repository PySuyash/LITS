# Write a program to print the factorial of a number

def calc_fact(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * calc_fact(num-1)

number = int(input("Enter number : "))

if number < 0:
    print(f"ERROR : Factorial of negative numbers is not possible.")
else:
    print(f"Factorial of '{number}' is : {calc_fact(number)}")