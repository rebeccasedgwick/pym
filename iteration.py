class Counter(object):
    def __init__(self, low, high):
        self.current = low
        self.high = high

    def __iter__(self):
        current = self.current
        while self.high >= current:
            yield current
            current += 1

# This version, using __iter__ allows reueable obj as the counter has no state
# given_obj = Counter(2, 10)
#
# for num in given_obj:
#     print(num, end='')
