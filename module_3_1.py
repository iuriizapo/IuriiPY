count = 0
def count_calls():
    global count
    count += 1

def string_info(string):
    result = (len(string), string.upper(), string.lower())
    count_calls()
    return result

def is_contains(string_, list_):
    string_ = string_.lower()
    for i in list_:
        list_ = i.lower()
        if list_ == string_:
            result = True
            break
        else:
            result = False

    count_calls()
    return result

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'urBAN', 'BaNaN']))
print(is_contains('cycle', ['recycling', 'cyclic']))

print(count)


