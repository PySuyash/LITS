# Write a program to print the reverse of a given number 

number = int(input("Enter number : "))

reverse = 0

while number > 0:
    rem = number%10
    reverse = reverse*10 + rem
    number = number//10

print(reverse)