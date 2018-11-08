def pallindrome(x):
    if x == x[::-1]:
        print("Yep, %s is a pallindrome" % x)
    else:
        print("Nope: %s is not a pallindrome" % x)
