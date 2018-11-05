amount = float(input("Enter an amount: £"))
interest_rate = float(input("Enter the interest rate (as decimal): "))
period = int(input("Enter period (number of years): "))
value = 0
year = 1
while year <= period:
    value = amount + (interest_rate * amount)
    print("Year %d: £%.2f" % (year, value))
    amount = value
    year += 1
