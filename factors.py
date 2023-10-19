import sys

#function to loop and start factorizing
def factorize(n):
    factors = [] #create list to append factors of input number
    for i in range(2, n//2 + 1): #loops over i from 2 to half n
        if n % i == 0:
            factors.append((i, n // i))
    return factors

if len(sys.argv) != 2: #check for input
    print("Usage: factors <file>")
    sys.exit(1)

try:
    with open(sys.argv[1], 'r') as file:
        lines = file.read().splitlines()

    for line in lines:
        n = int(line)
        factorizations = factorize(n)
        for p, q in factorizations:
            print(f"{n}={p}*{q}")

except FileNotFoundError:
    print(f"File {sys.argv[1]} not found.")
    sys.exit(1)

except ValueError:
    print("Invalid input in the file. Please ensure all lines are valid natural numbers.")
    sys.exit(1)

