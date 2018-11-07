a, b = 0, 1
# multiline print:
while b < 100:
    print(b)
    a, b = b, a + b

# single line print in py3:
x, y = 0, 1
while y < 100:
    print(y, end=" ")
    x, y = y, x + y

# single line print in py2:
# c, d = 0, 1
# while d < 100:
#     print(d),
#     c, d = d, c + d
