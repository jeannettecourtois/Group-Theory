Group Theory in Python

This repository gathers my experiments in group theory implemented in Python.
It contains scripts exploring modular arithmetic, cyclic groups, Euler’s totient function, and an application to RSA cryptography.

📂 Project Structure
.
├── group_1.py    # Basic constructions (Zn, equivalence classes, partitions, clock representation)
├── group_2.py    # Abstract base classes for groups, additive groups of integers, generators
├── group_3.py    # Euler's totient function, gcd, primality checks
├── RSA.py        # RSA cryptosystem (prime generation, keys, encryption/decryption)

🚀 Python Scripts Overview

group_1.py

Builds cartesian products and equivalence classes.

Implements Zn (integers modulo n) as a Python class.

Provides visualizations of modular classes on the unit circle.

Example: viewing a clock as Z/12Z.

group_2.py

Defines abstract groupe and a concrete additive group groupe_Z.

Includes methods for adding elements, computing symmetries, and homomorphisms.

Implements a generator class to produce cyclic subgroups.

group_3.py

Implements Euler’s totient function ϕ(n).

Functions: is_prime, pgcd, indicatrice_euler.

Illustrates arithmetic properties used in group theory.

RSA.py

Implements a basic RSA cryptosystem:

Prime generation

Key pair creation (public/private)

Encryption and decryption demo

Demonstrates the link between group theory and cryptography.

▶️ How to Run
# Run RSA demo
python RSA.py

# Visualize modular classes on the unit circle
python group_1.py


Requirements:

Python 3.x

numpy

matplotlib

🎯 Purpose

Practice Python programming alongside learning group theory.

Visualize and experiment with group structures.

Connect abstract algebra with real-world cryptographic applications.
