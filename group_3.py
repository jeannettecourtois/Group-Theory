import numpy as np 

def is_prime(n:int)->bool:
    divisors = []
    for i in range(1, n+1): 
        if n % i == 0:
            divisors.append(i)
    if len(divisors) == 2:
        return True 
    return False

def pgcd(a, b):
    if b<a:
        pgcd(b, a)
    while b != 0:
        t = b 
        b = a % b
        a = t
    return a 


def indicatrice_euler(n:int):
    primes_with = []
    if is_prime(n):
        return n-1 
    else: 
        for i in range(1, n+1):
            if pgcd(n, i) == 1:
                print(i)
                primes_with.append(i)
    return len(primes_with)
                
    


def main():
    print("Chapter 3 of group theory")
    print(indicatrice_euler(6))


if __name__ == "__main__":
    main()