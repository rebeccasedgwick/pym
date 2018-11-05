n = 5
total = 0
count = 0
while count < n:
    number = float(input(""))
    total += number
    count += 1
average = float(total) / n
print("n: %d, total: %f" % (n, total))
print("average: %f" % average)
