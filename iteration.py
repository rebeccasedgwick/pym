class Counter(object):
    def __init__(self, low, high):
        self.current = low
        self.high = high

    def __iter__(self):
        'Returns itself as an iterator object'
        return self

    def __next__(self):
        'Returns the enxt value, whilst current is lower than high value'
        if self.current > self.high:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1

# Example use:
#   counter = Counter(2,10)
#   for i in counter:
#       print(i, end=' ')
#
# >>> 2 3 4 5 6 7
#
# or:
#
# iterator = iter(c)
#
# while True:
#     try:
#         x = iterator.__next__()
#         print(x, end=' ')
#     except StopIteration as e:
#         break
