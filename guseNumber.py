from random import randint

print("система загадала число.....")
b = randint(1,100)


while True:
    a = int(input("введите число: "))
    if a == b:
        print("угодал")
        break
    elif a > b:
        print("не угодал число меньше" , b)

    elif a < b:
        print("не угодал число больше" , b)

