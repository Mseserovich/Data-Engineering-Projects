from string_calculator.calculator import add
import pytest


@pytest.mark.parametrize(
    "test_input, expected_output, message",
    [
        ("", 0, "Expected output is 0"),
        ("1", 1, "Expected output is 1"),
        ("1,1", 2, "Expected output is 2"),
        ("1\n1", 2, "Expected output is 2"),
    ],
)
def test_add_basic_input(test_input, expected_output, message):
    output = add(test_input)
    assert output == expected_output, message


@pytest.mark.parametrize(
    "test_input, expected_output, message",
    [
        ("//[:D][%]\n1:D2%3", 6, "Expected output of 6"),
        ("//[***][%%%]\n1***2%%%3", 6, "Expected output of 6"),
        ("//[(-_-')][%]\n1(-_-')2%3", 6, "Expected output of 6"),
        ("//[abc][777][:(]\n1abc27773:(1", 7, "Expected output is 7"),
    ],
)
def test_add_multiple_delimiters(test_input, expected_output, message):
    output = add(test_input)
    assert output == expected_output, message


@pytest.mark.parametrize(
    "test_input, expected_output, message",
    [
        (",10,10", ValueError, "Error: invalid input"),
        ("\n10", ValueError, "Error: invalid input"),
        ("//;\n10;100;1;1;", ValueError, "Error: invalid input"),
        ("//;\n1000;1;2;", ValueError, "Error: invalid input"),
        ("   //;\n1000,1;2", ValueError, "Error: invalid input"),
        ("1,2,3//;\n1000,1;2", ValueError, "Error: invalid input"),
    ],
)
def test_add_invalid_input(test_input, expected_output, message):
    with pytest.raises(ValueError) as e:
        add(test_input)
    assert e.type == expected_output, message


@pytest.mark.parametrize(
    "test_input, expected_output, message",
    [
        ("//,\n1,1,-2",ValueError,"Raises a ValueError exception")
    ],
)
def test_negative_numbers(test_input, expected_output, message):
    with pytest.raises(ValueError) as exc_info:
        add(test_input)
    assert exc_info.type == expected_output, message

@pytest.mark.parametrize("test_input, expected_output, message",
                        [
                            ("1\n1", 2, "The expected output is 2"),
                            ("1\n2\n3\n4", 10, 'The expected output is 10')
                        ])
def test_new_line(test_input, expected_output, message):
    output = add(test_input)
    assert output == expected_output, message

def test_empty_string():
    output = add("")
    assert output == 0, "The expected output is 0"

@pytest.mark.parametrize("test_input, expected_output, message",
                        [
                            ("1,2,3,4,5", 15, "The expected output is 15"),
                            ("1\n2\n4\n7\n9", 23, "The expected output is 23")
                        ])
def test_multiple_integers(test_input, expected_output, message):
    output = add(test_input)
    assert output == expected_output, message

@pytest.mark.parametrize("test_input, expected_output, message",
                        [
                            ("1000", 0, "The expected output is 0"),
                            ("1,999,1000", 1000, "The expected output is 1000")
                        ])
def test_integers_above_1000(test_input, expected_output, message):
    output = add(test_input)
    assert output == expected_output, message