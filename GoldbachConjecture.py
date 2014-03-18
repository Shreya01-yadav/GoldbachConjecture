# Goldbach Conjecture Verifier
from math import sqrt

primes = [2, 3]
GoldbachNumbers = {4: [2, 2]}

# Return true if N is prime. Assumes all primes up to sqrt(N) are known.
def isPrime(n):
        lastFactor = sqrt(n)
        for i in primes:
                if i > lastFactor:
                        return True
                if n % i == 0:
                        return False

# Find primes up to N and append them to primes
def findPrimes(n):
        for i in range(primes[-1] + 2, n, 2):
                if isPrime(i):
                        primes.append(i)

# Append {N: [prime pairs that sum to N]} to GoldbachNumbers
def Goldbach(n):
        if n not in GoldbachNumbers:
                if n > primes[-1]:
                        findPrimes(n)
                GoldbachNumbers[n] = []
                for i in primes:
                        if i > n/2:
                                break
                        if n - i in primes:
                                GoldbachNumbers[n].extend([i, n - i])

# Find the prime possibilities for all numbers up to N
def findGoldbachs(n):
        for i in range(max(GoldbachNumbers) + 2, n + 1, 2):
                Goldbach(i)

# Load the list of prime numbers into primes
primeFile = open('Primes.txt', 'r+')
for line in primeFile:
        line = int(line)
        if primes.count(line) == 0:
                primes.append(line)
numPrimesInFile = len(primes)

# Load the list of Goldbach pieces into GoldbachNumbers
GoldbachFile = open('Goldbach.txt', 'r+')
for line in GoldbachFile:
        line = line.split()
        n = int(line[0])
        if n not in GoldbachNumbers:
                GoldbachNumbers[n] = []
                for i in line[1:]:
                        i = int(i)
                        GoldbachNumbers[n].extend([i, n - i])
numGoldbachsInFile = len(GoldbachNumbers.keys())

# I/O loop
x = 2
while x > 0:
        x = int(input('Enter an even number: '))
        # x = 10000
        findGoldbachs(x)
        print(GoldbachNumbers[x])

# Save any newly generated primes and Goldbach pieces
for i in primes[numPrimesInFile:]:
        primeFile.write(str(i) + '\n')
primeFile.close()
for i in sorted(GoldbachNumbers.keys())[numGoldbachsInFile:]:
        GoldbachFile.write(str(i))
        for x in GoldbachNumbers[i][::2]:
                GoldbachFile.write(' ' + str(x))
        GoldbachFile.write('\n')
GoldbachFile.close()
