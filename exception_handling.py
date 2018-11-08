def holla_at_me():
    word = int(input("Word UP! Give me a number: "))
    return word


while True:
    try:
        print(holla_at_me())
    except ValueError:
        print("Nacht, I don't translate roman numerals.")
