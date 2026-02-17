# Write a program to check wheather a number is prime or not

def isPrime(num):
    if num == 1:
        return f"{num} is not prime"
    elif num == 2:
        return f"{num} is prime"
    else:
        for i in range(2, num):
            if num%i == 0:
                return f"{num} is not prime"
            return f"{num} is prime"

num = int(input("Number : "))
print(isPrime(num))