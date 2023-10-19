#!/usr/bin/python3
import sympy

def factorize_rsa_challenge(filename):
    with open(filename, 'r') as file:
        for line in file:
            n = int(line.strip())
            p, q = sympy.ntheory.factor_.factorint(n).keys()
            print(f"{n}={p}*{q}")

if __name__ == '__main__':
    file_to_factorize = 'tests/rsa-1'  # Provide the path to your test file
    factorize_rsa_challenge(file_to_factorize)

