def absValue(x):
    if x < 0:
        return -x
    else:
        return x

#fast exponentiation used
def power(x, p):
    if p == 0:
        return 1
    elif p == 1:
        return x

    pow_2 = power(x,p//2)
    if p % 2 == 0:
        return pow_2 * pow_2
    else:
        return pow_2 * pow_2 * x

#fast search done
def isPrime(x):
    if x<2:
        return False
    c = 2
    while c * c <= x:
        if x % c == 0:
            return False
        c += 1
    return True

#slow fib
def slowFib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return slowFib(n-2) + slowFib(n-1)

#quick fib
def quickFib(n):
    a = 0
    b = 1
    for _ in range(n):
        a, b = b, a + b
    return a


