# 7-Cree una función que acepte una lista de números y retorne una lista con los números primos de la misma.

def is_prime(number):
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


def filter_primes(numbers):
    primes = []
    for num in numbers:
        if is_prime(num):
            primes.append(num)
    return primes


numbers = [1, 4, 6, 7, 13, 9, 67, 27, 99, 54, 41]
result = filter_primes(numbers)
print(result)
