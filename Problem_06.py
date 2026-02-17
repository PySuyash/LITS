# Write a program to check wheather a number is divisible by 5 and 11 or not

num = int(input("Number : "))

if (num%5 == 0 and num%11 == 0):
    print(f"{num} is divisible by 5 and 11")

else:
    print(f"Not divisible")