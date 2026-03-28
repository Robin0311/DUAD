from ejercicio_7 import filter_primes


def test_filter_primes_with_mixed_numbers():
    # Arrange
    numbers = [1, 4, 6, 7, 13, 9, 67]
    expected = [7, 13, 67]

    # Act
    result = filter_primes(numbers)

    # Assert
    assert result == expected


def test_filter_primes_with_only_primes():
    # Arrange
    numbers = [2, 3, 5, 7, 11]
    expected = [2, 3, 5, 7, 11]

    # Act
    result = filter_primes(numbers)

    # Assert
    assert result == expected


def test_filter_primes_with_no_primes():
    # Arrange
    numbers = [0, 1, 4, 6, 8, 9, 10, -3, -5]
    expected = []

    # Act
    result = filter_primes(numbers)

    # Assert
    assert result == expected
