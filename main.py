print("Hello, If you want to see my biography, please enter the password: ")


def info():
    print("Привет, я Жавохир Саиткулов, 2002 года рождения. Я из города Шымкент.")


while True:
    password = input("Enter the password: ")
    if password == "pass":
        info()
        break
    else:
        print("Password is not correct, Try again!")
