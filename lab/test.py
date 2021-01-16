def search(f):
    x = 0
    while True:
        if (f(x)):
            return x
        x = x + 1

def is_three(x):
    return x == 3

def positive(x):
    return max(0, x * x - 100)

def square(x):
    return x * x

def inverse(f):
    return lambda y: search(lambda x: f(x) == y)