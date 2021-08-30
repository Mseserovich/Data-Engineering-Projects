from validate_id.validation import *
import pytest

@pytest.mark.parametrize("id_num, expected_output, message",
                            [
                                ("2909035800085", True, "Test string should return True"),
                                ("2001014800086", True, "Test string should return True")
                            ])
def test_is_id_number_valid(id_num, expected_output, message):
    output = is_id_number_valid(id_num)
    assert output == expected_output, message

@pytest.mark.parametrize("id_num, expected_output, message",
                            [
                                ("084738928374839", False, "ID number is too long"),
                                ("[728971983272", False, "Invalid characters contained in ID"),
                                ("124", False, "ID number is too short")
                            ])
def test_is_input_valid(id_num, expected_output, message):
    output = is_input_valid(id_num)
    assert output == expected_output , message

def test_is_constant_valid():
    output = is_constant_valid("2001014800086")
    assert output == True, "Constant digit value incorrect"

def test_is_checksum_valid():
    output = is_checksum_valid("2909035800085")
    assert output == True, "Checksum value not equal"

def test_is_citizen_valid():
    output = is_citizen_valid("2001014800086")
    assert output == True, "citizen value is incorrect"

@pytest.mark.parametrize("day, month, year, expected_output, message",
                        [
                            ("30", "02", "2000", False, "date is invalid"),
                            ("29", "02", "2000", True, "date is valid")
                        ])
def test_is_date_valid(day, month, year, expected_output, message):
    output = is_date_valid(day, month, year)
    assert output == expected_output, message

