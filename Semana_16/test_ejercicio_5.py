from ejercicio_5 import count_case


def test_count_case_mixed_text():
    # Arrange
    text = "I love Nación Sushi"
    expected = "There are 3 upper cases and 13 lower cases"

    # Act
    result = count_case(text)

    # Assert
    assert result == expected


def test_count_case_all_uppercase():
    # Arrange
    text = "HELLO WORLD"
    expected = "There are 10 upper cases and 0 lower cases"

    # Act
    result = count_case(text)

    # Assert
    assert result == expected


def test_count_case_all_lowercase():
    # Arrange
    text = "python is awesome"
    expected = "There are 0 upper cases and 15 lower cases"

    # Act
    result = count_case(text)

    # Assert
    assert result == expected
