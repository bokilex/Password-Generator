import random
input001 = input("How much passwords you want to make?")
input002 = input("How much characters you want from your password to have?")

chars = 'qwertyuiopasdfghjklzxcvbm!@#$%^&*()1234567890'

number = int(input001)
length = int(input002)
for p in range(number):
    password = ''
    for c in range(length):
        password += random.choice(chars)
    print("Your password is:\n")
    print(password)
