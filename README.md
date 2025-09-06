# 🔢 Group Theory in Python  

This repository is a personal playground to explore **group theory** through Python.  
It mixes abstract algebra (ℤ/nℤ, cyclic groups, Euler’s totient function) with practical applications such as **RSA cryptography**.  

---

## 📂 Files  

- **`group_1.py`**  
  ℤ/nℤ implementation, equivalence classes, cartesian products, and clock representation.  
  → Visualize modular arithmetic on the **unit circle** 🕒  

- **`group_2.py`**  
  Abstract base class `groupe` and additive group of integers.  
  → Includes **symmetries, homomorphisms**, and cyclic subgroup generators. ⚡  

- **`group_3.py`**  
  Implements number theory tools:  
  - `is_prime(n)` 🔍  
  - `pgcd(a, b)` (gcd)  
  - `indicatrice_euler(n)` = Euler’s φ(n) function  
  → Useful for studying the multiplicative group (ℤ/nℤ)×.  

- **`RSA.py`**  
  A simple **RSA cryptosystem** 🔐  
  - Prime generation  
  - Public/private key pair  
  - Encryption & decryption demo  

---

## ▶️ How to Run  

Clone the repository and run any script:  

```bash
# RSA demo
python RSA.py

# Modular arithmetic visualizations
python group_1.py

