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
                primes_with.append(i)
    return len(primes_with), primes_with

#multiplicative group 

class Z_n_N_x:
    def __init__(self, n):
        self._n = n 
        self._classes_equivalences = []
        
    @property 
    def n(self):
        return self._n
    
    @property
    def classes_equivalences(self):
        return self._classes_equivalences
    
    @classes_equivalences.setter
    def classes_equivalences(self, value):
        self._classes_equivalences = [i for i in range(1, self._n) if pgcd(self._n, i) == 1]

    
    
                
    


def main():
    print("Chapter 3 of group theory")
    Z_3_Z = Z_n_N_x(3)
    Z_3_Z.classes_equivalences = None #the calculation is done
    print(Z_3_Z._classes_equivalences)


if __name__ == "__main__":
    main()