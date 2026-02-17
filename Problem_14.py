# Write a program to print the fibonacci series upto 10 terms

a, b = 0, 1

for i in range(1, 11):
    print(a, end=" ")
    a,b = b, a+b