import random

secret_number = random.randint(1,10)
secret = []


while True:
    try:    
        print("Please enter your number")
        guess = int(input("->"))
        secret.append(guess)
        if len(secret) >= 5:
            print('Good luck next time')
            break
        elif guess == secret_number:
            print("Good job")
        elif guess != secret_number:
            print("that's not it")

    except ValueError:
        print("{} is not a valid number".format(guess))