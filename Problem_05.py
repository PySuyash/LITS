# Write a program to check whether a given character is a vowel or consonant

char = input("Character : ")

vowel = ['a', 'e', 'i', 'o',' u']

if char.lower() in vowel:
    print(f"{char} is vowel")
else:
    print(f"{char} is consonant")