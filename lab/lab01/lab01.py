def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    "*** YOUR CODE HERE ***"
    acc = 1
    depth = k
    while(k > 0):
        acc = acc * (n - (depth - k))
        k = k - 1
    print(acc)        
            
    



def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    "*** YOUR CODE HERE ***"
    # sum = 0
    # for n in list(str(y)):
    #     sum += int(n)
    # return sum
    if y < 10:
        return y
    else:
        cur = y % 10
        next = y // 10
        return cur + sum_digits(next)


def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
    # count = 0
    # for number in list(str(n)):
    #     if number == "8":
    #         count += 1
    #     else:
    #         count = 0
    #     if count == 2:
    #         return True

    # return False
    sum = 0
    while (n > 1):
        if n % 10 == 8:
            sum += 1
        else: 
            sum = 0
        if sum ==2:
            return True
        n = n // 10
    return False

def cube(n):
    return pow(n, 3)

def sum_total(n, fn):
    total, k = 0, 1
    while k <= n:
        total, k = total + fn(k), k + 1
    
    return total

c


        

