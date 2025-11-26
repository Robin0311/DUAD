# 7-Cree una función que acepte una lista de números y retorne una lista con los números primos de la misma.

def is_prime(number):
    # Números menores o iguales a 1 NO son primos (incluye negativos, 0 y 1)
    if number <= 1:
        return False

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


if __name__ == "__main__":
    numbers = [1, 4, 6, 7, 13, 9, 67, 27, 99, 54, 41]
    result = filter_primes(numbers)
    print(result)
