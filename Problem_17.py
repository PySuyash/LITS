# Write a program to find the sum of numbers from 1 to n

n = int(input("Enter n : "))

S = 0

for i in range(1, n+1):
    S += i

print(f"The sum of 1 to {n} terms is : {S}")