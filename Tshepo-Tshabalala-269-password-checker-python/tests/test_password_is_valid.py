from password_checker.password_checker import password_is_valid, password_strength
import pytest


def test_empty_string():
    with pytest.raises(ValueError) as error_info:
        password_is_valid("")
    assert str(error_info.value) == "password should exist"


@pytest.mark.parametrize(
    "test_input, expected_output, message",
    [
        ("a", ValueError, "password should be longer than 8 characters"),
        ("djhM3", ValueError, "password should be longer than 8 characters"),
    ],
)
def test_character_length(test_input, expected_output, message):
    with pytest.raises(expected_output) as error_info:
        password_is_valid(test_input)
    assert str(error_info.value) == message


@pytest.mark.parametrize(
    "test_input, expected_output, message",
    [
        (
            "abcdhsslkjh",
            ValueError,
            "password should have at least one uppercase letter",
        ),
        (
            "mseserovich#",
            ValueError,
            "password should have at least one uppercase letter",
        ),
    ],
)
def test_uppercase(test_input, expected_output, message):
    with pytest.raises(expected_output) as error_info:
        password_is_valid(test_input)
    assert str(error_info.value) == message


@pytest.mark.parametrize(
    "test_input, expected_output, message",
    [
        ("Aaaaaaaaaaa", ValueError, "password should at least have one digit"),
        ("UHSLhldh*aa", ValueError, "password should at least have one digit"),
    ],
)
def test_digit(test_input, expected_output, message):
    with pytest.raises(expected_output) as error_info:
        password_is_valid(test_input)
    assert str(error_info.value) == message


@pytest.mark.parametrize(
    "test_input, expected_output, message",
    [
        (
            "A1aaaaaaaaa",
            ValueError,
            "password should have at least one special character",
        ),
        (
            "MseoiT 111",
            ValueError,
            "password should have at least one special character",
        ),
    ],
)
def test_special_character(test_input, expected_output, message):
    with pytest.raises(expected_output) as error_info:
        password_is_valid(test_input)
    assert str(error_info.value) == message


@pytest.mark.parametrize(
    "test_input, expected_output, message",
    [
        (
            "$1Aaaaaaaaa",
            ValueError,
            "password should have at least one whitespace character",
        ),
        (
            "Jon-doe200",
            ValueError,
            "password should have at least one whitespace character",
        ),
    ],
)
def test_whitespace(test_input, expected_output, message):
    with pytest.raises(expected_output) as error_info:
        password_is_valid(test_input)
    assert str(error_info.value) == message


@pytest.mark.parametrize(
    "test_input, expected_output, message",
    [
        (
            "$1A AAAAAAA",
            ValueError,
            "password should have at least one lowercase letter",
        ),
        ("$POM 6@1W", ValueError, "password should have at least one lowercase letter"),
    ],
)
def test_lowercase(test_input, expected_output, message):
    with pytest.raises(expected_output) as error_info:
        password_is_valid(test_input)
    assert str(error_info.value) == message


@pytest.mark.parametrize(
    "test_input, expected_output, message",
    [
        ("", "invalid", "expected output is ---> 'invalid'"),
        ("a", "invalid", "expected output is ---> 'invalid'"),
        ("AAAa ", "invalid", "expected output is ---> 'invalid'"),
    ],
)
def test_invalid_password(test_input, expected_output, message):
    output = password_strength(test_input)
    assert output == expected_output, message


@pytest.mark.parametrize(
    "test_input, expected_output, message",
    [
        ("aaaaaaaaaa", "weak", "expected output is ---> 'weak'"),
        ("AAAAAAAAAA", "weak", "expected output is ---> 'weak'"),
        ("1111111111", "weak", "expected output is ---> 'weak'"),
    ],
)
def test_weak_password(test_input, expected_output, message):
    output = password_strength(test_input)
    assert output == expected_output, message


@pytest.mark.parametrize(
    "test_input, expected_output, message",
    [
        (" aAaaaaaaaa", "medium", "expected output is ---> 'medium'"),
        ("aAaaaaaaaa%", "medium", "expected output is ---> 'medium'"),
    ],
)
def test_medium_password(test_input, expected_output, message):
    output = password_strength(test_input)
    assert output == expected_output, message


@pytest.mark.parametrize(
    "test_input, expected_output, message",
    [
        ("$1Aaaaaaaaa", "strong", "expected output is ---> 'strong'"),
        (" $1Aaaaaaaaa", "strong", "expected output is ---> 'strong'"),
    ],
)
def test_strong_password(test_input, expected_output, message):
    output = password_strength(test_input)
    assert output == expected_output, message
