
from ejercicio_3 import sum_elements


def test_sum_elements_with_small_positive_numbers():
    # Arrange
    numbers = [4, 6, 2, 29]
    expected_result = 41

    # Act
    result = sum_elements(numbers)

    # Assert
    assert result == expected_result


def test_sum_elements_with_negative_numbers():
    # Arrange
    numbers = [-5, 10, -3]
    expected_result = 2

    # Act
    result = sum_elements(numbers)

    # Assert
    assert result == expected_result


def test_sum_elements_with_mixed_integers_and_zero():
    # Arrange
    numbers = [0, 100, 200, 0]
    expected_result = 300

    # Act
    result = sum_elements(numbers)

    # Assert
    assert result == expected_result
