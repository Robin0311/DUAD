from ejercicio_6 import sort_string_alphabetically


def test_sort_string_alphabetically_example_case():
    # Arrange
    text = "python-variable-funcion-computadora-monitor"
    expected = "computadora-funcion-monitor-python-variable"

    # Act
    result = sort_string_alphabetically(text)

    # Assert
    assert result == expected


def test_sort_string_alphabetically_names():
    # Arrange
    text = "Robinson-Isabel-Tabata-Alex-Bryan-Maria"
    expected = "Alex-Bryan-Isabel-Maria-Robinson-Tabata"

    # Act
    result = sort_string_alphabetically(text)

    # Assert
    assert result == expected


def test_sort_string_alphabetically_single_word():
    # Arrange
    text = "Python"
    expected = "Python"  # no hay guiones, no cambia

    # Act
    result = sort_string_alphabetically(text)

    # Assert
    assert result == expected
