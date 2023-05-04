#!/usr/bin/env python3

def factorial(n):
    """
    Calcula el factorial de n mediante un codigo iterativo con la estructura for
    """
    f = 1
    for i in range(1,n+1): #[1,10) el ultimo valor es el de parada
        f *= i
    return f

def factorial_rec(n):
    if n == 0:
        return 1
    else:
        return n * factorial_rec(n-1)
        

def main():
    print(factorial(5))

if __name__ == '__main__':
    main()



#las listas no son listas son vectores 