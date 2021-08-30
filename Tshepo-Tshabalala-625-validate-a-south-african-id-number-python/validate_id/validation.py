from datetime import date

def is_id_number_valid(id_num):
    valid = [
                is_input_valid(id_num),
                is_date_valid(id_num[4:6], id_num[2:4], id_num[0:2]),
                is_checksum_valid(id_num), is_constant_valid(id_num),
                is_citizen_valid(id_num)
            ]
    return all(valid)

def is_constant_valid(id_num):
    return id_num[11] == '8'
    
def is_input_valid(id_num):
    id_len = len(id_num)
    if id_len != 13:
        return False
    elif not id_num.isnumeric():
        return False
    else:
        return True

def is_date_valid(day, month, year):
    valid_date = True
    try:
        date(int(year), int(month), int(day))
    except ValueError:
        valid_date = False
    finally:
        return valid_date

def convert_to_digits(num):
    return [int(i) for i in str(num)]

def is_checksum_valid(id_num):
    digits = convert_to_digits(id_num)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = sum(odd_digits)
    for i in even_digits:
        checksum += sum(convert_to_digits(i * 2))
    return checksum % 10 == 0

def is_citizen_valid(id_num):
    return id_num[10] == '0' or id_num[10] == '1'