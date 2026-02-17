# Write a program to calculate the sum of digits of a number.

number = int(input("Enter a number : "))

number = abs(number)

num = number 

digit_sum = 0

while number > 0:
    rem = number%10
    digit_sum += rem
    number //= 10

print(f"The sum of digits of {num} : {digit_sum}")