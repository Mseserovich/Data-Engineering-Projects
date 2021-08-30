import re


def add(string):
    assert type(string) == str, "Argument must be string only"
    pattern = r"^(//(?=\[)*(?P<delim>.+?)(?!\])*\n){0,1}(?P<numbers>-?\d+((.+?|,|\n)-?\d+){0,}){0,}$"
    if string == '':
        return 0
    match = re.search(pattern, string, re.DOTALL)
    try:
        numbers = match.group("numbers")
        if match.group("delim") != None:
            delimiters = re.findall(r"\[*(.+?)\]*", match.group("delim"))
            for item in delimiters:
                numbers = numbers.replace(item, ',')
        if '-' in numbers:
            negatives = ",".join(re.findall(r"-\d", numbers))
            raise ValueError(f"Error: negatives not allowed {negatives}")
        if re.search("[^0-9,\n]", numbers):
            raise ValueError("Error: invalid input")
        all_digits = re.findall(r"\d+", numbers)
        integers = [int(num) for num in all_digits if int(num) < 1000]
        return sum(integers)
    except AttributeError:
        raise ValueError("Error: invalid input")