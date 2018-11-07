# Couple of basic enumerate() uses:
# Ultimately, enumerate() is useful to keep a count of iterations
# The enumerate obj that is returned from this method can be used directly -
# either in for loops (etc) or it can be converted into a list of tuples using
# the list() method.

'''
enumerate(iterable, start=0)

Parameters:
Iterable: any object that supports iteration
Start: the index value from which the counter is
              to be started, by default it is 0
'''


teas = ['assam', 'darjeeling', 'lapsang souchong', 'oolong']

print("Print an enumerate that's been created from a list:")
for tea in enumerate(teas):
    print(tea)

# RETURNED:
    # (0, 'assam')
    # (1, 'darjeeling')
    # (2, 'lapsang souchong')
    # (3, 'oolong')
print('\n')
print("Print the 'count, item' for an enumerate:")
for count, item in enumerate(teas):
    print(count, item)

# RETURNED:
    # 0 assam
    # 1 darjeeling
    # 2 lapsang souchong
    # 3 oolong

print('\n')
# You can change the default start value that the counter beings at.
# The args format is: enumerate(iterable, start=0)
# The default start value is 0. Here, it's changed to start at 100:

print("Change the start count value:")
for count, item in enumerate(teas, 100):
    print(count, item)
print('\n')
print('\n')
print("Deviation: using zip()")
# Side note: to iterate over a couple sequences simultaneously, use zip()

first_names = ('alice', 'bob', 'charlie')
last_names = ('wonderland', "l'eponge", 'horse')

full_names = zip(first_names, last_names)
print("This is a zipped object created from a list:")
print(full_names)

print('\n')
print("Use tuple() to make a printable / readable version of the result:")
print(tuple(full_names))

# or to actually use this in practice:
print('\n')
print("Use zip() in practice by interpolating first & last names in a string:")
for first, last in zip(first_names, last_names):
    print("%s's surname is %s" % (first, last))
