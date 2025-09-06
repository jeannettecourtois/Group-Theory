#cryptographie modulaire (RSA, Diffie-Hellman, etc)
from typing import List
import random 
import math 

def is_prime(number:int):
    if number < 2:
        return False 
    for i in range(2, number//2 + 1): #pas besoin d'aller jusqu'à la fin
        if number % i == 0:
            return False
    return True 





def generate_prime(min_value: int, max_value: int) -> int:
    while True:
        candidate = random.randint(min_value, max_value)
        if is_prime(candidate):
            return candidate

#retourner la clé privée 
def mod_inverse(e, phi):
    for d in range(3, phi):
        if (d * e) % phi == 1:
            return d 
    raise ValueError("mod_inverse does not exist")


def __main__():
    
    print("Tests: ")
    
    p, q = generate_prime(1000, 5000), generate_prime(1000, 5000)
    while p == q:
        q = generate_prime(1000, 5000)
   
    n = p * q
    
    phi_n = (p-1)*(q-1)
    
    e = random.randint(3, phi_n-1)
    #gcd() method returns the greatest common divisor of the two integers int1 and int2
    
    
    while math.gcd(e, phi_n) != 1:
        e = random.randint(3, phi_n) #problème avec e 

    
    d = mod_inverse(e, phi_n)
    print("Public key: ", e)
    print("Private Key: ", d)
    print("n: ", n)
    print("Phi of n: ", phi_n)
    print("p:", p)
    print("q: ", q)
    message = "Hello"
    message_encoded = [ord(ch) for ch in message]
    cipher = [pow(ch, e, n) for ch in message_encoded]
    decrypted = [pow(ch, d, n) for ch in cipher]
    decoded_message = " ".join(chr(ch) for ch in decrypted)
    print("Encryoted: ", cipher)
    print("Decrypted: ", decoded_message)
    
    
    
if __name__ == "__main__":
    __main__()