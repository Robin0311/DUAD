from ejercicio_4 import reverse_string


def test_reverse_string_regular_word():
    # Arrange
    text = "Hola"
    expected = "aloH"

    # Act
    result = reverse_string(text)

    # Assert
    assert result == expected


def test_reverse_string_with_spaces():
    # Arrange
    text = "Hola mundo"
    expected = "odnum aloH"

    # Act
    result = reverse_string(text)

    # Assert
    assert result == expected


def test_reverse_string_with_special_characters():
    # Arrange
    text = "Python 3.11!"
    expected = "!11.3 nohtyP"

    # Act
    result = reverse_string(text)

    # Assert
    assert result == expected
