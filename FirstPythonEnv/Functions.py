def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
        else:
            return True

#if isPrime(n):
#    print(f'{n} is prime number')
#else:
#    print(f'{n} is not a prime number')

def list_primes():
    for x in range(100):
        if isPrime(x):
            print(x, end=' ', flush=True)
    print()

list_primes()