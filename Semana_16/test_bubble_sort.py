import pytest
from bubble_sort import bubble_sort


def test_bubble_sort_works_with_small_list():
    # Arrange
    input_list = [5, 3, 8, 1, 2]
    expected_result = [1, 2, 3, 5, 8]

    # Act
    result = bubble_sort(input_list)

    # Assert
    assert result == expected_result
    assert input_list == expected_result


def test_bubble_sort_works_with_big_list():
    # Arrange
    input_list = list(range(200, 0, -1))
    expected_result = list(range(1, 201))

    # Act
    result = bubble_sort(input_list)

    # Assert
    assert result == expected_result
    assert input_list == expected_result
    assert len(result) == len(input_list)


def test_bubble_sort_works_with_empty_list():
    # Arrange
    input_list = []
    expected_result = []

    # Act
    result = bubble_sort(input_list)

    # Assert
    assert result == expected_result
    assert input_list == expected_result


def test_bubble_sort_raises_type_error_when_not_list():
    # Arrange
    input_value = "not a list"

    # Act / Assert
    with pytest.raises(TypeError):
        bubble_sort(input_value)
