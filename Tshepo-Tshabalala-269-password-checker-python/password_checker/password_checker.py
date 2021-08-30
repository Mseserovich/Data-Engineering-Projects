import re
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("errors.log")
file_handler.setLevel(logging.ERROR)

stream_handler = logging.StreamHandler()

logger.addHandler(file_handler)
logger.addHandler(stream_handler)
ERROR_MESSAGES = [
    "password should exist",
    "password should be longer than 8 characters",
    "password should have at least one uppercase letter",
    "password should have at least one lowercase letter",
    "password should at least have one digit",
    "password should have at least one special character",
    "password should have at least one whitespace character",
]


def password_is_valid(password):
    condition = match_password(password)
    for i in range(len(condition)):
        if not condition[i]:
            logger.error(ERROR_MESSAGES[i])
            raise ValueError(ERROR_MESSAGES[i])
    return True


def match_password(password):
    condition = []
    condition_list = [
        r"[A-Z]",
        r"[a-z]",
        r"\d",
        r"[\"`[@_!#\$%\^&\*\(\)<'>\?\/\|\}\{~,;:\+\.\]\\=-]",
        r"\s",
    ]
    condition.append(False) if len(password) == 0 else condition.append(True)
    condition.append(True) if len(password) > 8 else condition.append(False)
    for raw_string in condition_list:
        if re.findall(raw_string, password):
            condition.append(True)
        else:
            condition.append(False)
    return condition


def password_strength(password):
    condition = match_password(password)
    if condition[0] != True or condition[1] != True:
        return "invalid"
    total_sum = sum(item for item in condition if item == True)
    if total_sum == 3:
        return "weak"
    elif total_sum > 3 and total_sum < 6:
        return "medium"
    elif total_sum >= 6:
        return "strong"


def password_is_ok(password):
    strength = password_strength(password)
    if strength == "invalid":
        logger.debug("User password is not ok")
        return False
    else:
        logger.debug("User password is ok")
        return True


if __name__ == "__main__":
    print(password_is_ok("hg"))
