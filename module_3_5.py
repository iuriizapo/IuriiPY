def get_multiplied_digits(number):
    str_number = str(number)
    if len(str_number) == 1:
        return int(str_number[0])
    else:
        first = int(str_number[0])
        return first * get_multiplied_digits(int(str_number[1:]))


result = get_multiplied_digits(123450)
print(result)

