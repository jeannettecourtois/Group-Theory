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


        
#additive group 

class Z_n_Z:
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
        self._classes_equivalences = [i for i in range(self._n)]
    
    def ordre_de_classe(self, value)->int:
        if value>= 0 and value < self._n:
            return self._n/pgcd(self._n, value)
        else: 
            value = value % self._n
            return self._n/pgcd(self._n, value)

def fermat_little_theorem(p:int)->list:
    list_of_valid = []
    if is_prime(p):
        for i in range(p):
            if pgcd(p, i) == 1 and (i**(p-1) % p) == 1 :
                list_of_valid.append(i)
        return list_of_valid
    else: 
        raise Exception("The element needs to be prime! ")

def main():
    print("Try examples here")
    # Z_12_Z = Z_n_Z(12)
    # Z_12_Z.classes_equivalences = None 
    # for i in range(12):
    #     if Z_12_Z.ordre_de_classe(i) == 12:
    #         print(i)
    # print(indicatrice_euler(18))
    print(indicatrice_euler(2))



if __name__ == "__main__":
    main()