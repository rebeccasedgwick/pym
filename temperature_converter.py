# Convert Celsius to Farenheit: C = F(-32) / 1.8
farenheit = 0.0
print("For the Americans:")
print("   F      C ")
while farenheit <= 200:
    celsius = (farenheit - 32.0) / 1.8
    print("%5.1f %7.2f" % (farenheit, celsius))
    farenheit += 10

print("")
# convert Farenheit to Celsius: F = (C * 1.8) + 32
c2 = 0.0
print("For literally everyone else:")
print("   C      F ")
while c2 <= 100:
    f2 = (c2 * 1.8) + 32
    print("%5.1f %7.2f" % (c2, f2))
    c2 += 5
