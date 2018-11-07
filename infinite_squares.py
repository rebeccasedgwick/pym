while True:
    n = int(input("Please enter an integer: "))
    if n < 0:
        print("Sorry, please enter a positive value")
        continue
    elif n == 0:
        break
    print("The square of your number is ", n ** 2)
print("Au revior")
