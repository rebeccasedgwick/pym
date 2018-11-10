def decorator(func):
    def wrapper(*args, **kwargs):
        print('Before call')
        result = func(*args, **kwargs)
        print('After call')
        return result
    return wrapper


@decorator
def add(a, b):
    'This is an add function'
    return a + b
