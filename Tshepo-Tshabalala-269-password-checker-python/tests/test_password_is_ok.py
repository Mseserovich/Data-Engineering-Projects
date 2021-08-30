from password_checker.password_checker import password_is_ok
import pytest


def test_for_levelname(caplog):
    password_is_ok("Msese 10$..")
    for record in caplog.records:
        assert record.levelname == "DEBUG"


@pytest.mark.parametrize(
    "test_input, error_message, message",
    [
        (
            "johndoe__1%",
            "User password is ok",
            "Password should be ok for medium passwords.",
        ),
        (
            "Msese rock=xk",
            "User password is ok",
            "Password should be ok for medium passwords.",
        ),
        (
            "Mavusofana10",
            "User password is ok",
            "Password should be ok for medium passwords.",
        ),
    ],
)
def test_for_medium_passwords(caplog, error_message, test_input, message):
    password_is_ok(test_input)
    assert error_message in caplog.text, message


@pytest.mark.parametrize(
    "test_input, expected_output, message",
    [
        (
            "dhghddmddkjjfa",
            True,
            "Return True for passwords with 3 matches.",
        ),
        (
            "Qwertyuykjkjl",
            True,
            "Return True for passwords with 4 matches.",
        ),
        (
            "mseseasaD4",
            True,
            "Return True for passwords with 5 matches.",
        ),
        (
            "mdmdmm dmdD4",
            True,
            "Return True for passwords with 6 matches.",
        ),
        (
            "aBcdefg 1%",
            True,
            "Returns True for passwords with 7 matches",
        ),
        (
            "",
            False,
            "Returns False for invalid passwords.",
        ),
    ],
)
def test_password_is_ok(test_input, expected_output, message):
    test_output = password_is_ok(test_input)
    assert test_output == expected_output, message


@pytest.mark.parametrize(
    "test_input, log_message, message",
    [
        (
            "abcdefghij",
            "User password is ok",
            "Password should be ok for weak passwords",
        ),
        (
            "Mseseseseses",
            "User password is ok",
            "Password should be ok for weak passwords",
        ),
    ],
)
def test_for_weak_passwords(caplog, test_input, log_message, message):
    password_is_ok(test_input)
    assert log_message in caplog.text, message


@pytest.mark.parametrize(
    "test_input, log_message, message",
    [
        (
            "MseseRovich1%",
            "User password is ok",
            "Password should be ok for weak passwords",
        ),
        (
            "Msese rovich7$",
            "User password is ok",
            "Password should be ok for weak passwords",
        ),
    ],
)
def test_for_strong_passwords(caplog, test_input, log_message, message):
    password_is_ok(test_input)
    assert log_message in caplog.text, message


@pytest.mark.parametrize(
    "test_input, error_message, message",
    [
        (
            "",
            "User password is not ok",
            "Password should not be ok for invalid passwords",
        ),
        (
            "msese",
            "User password is not ok",
            "Password should not be ok for invalid passwords",
        ),
    ],
)
def test_for_invalid_passwords(caplog, test_input, error_message, message):
    password_is_ok(test_input)
    assert error_message in caplog.text, message
