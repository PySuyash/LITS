# Write a program to find the first multiple of 7 greater than 50 (using break).

for i in range(51, 100):
    if i % 7 == 0:
        print(f"First multiple of 7 greater than 50 : {i}")
        break