import re
def extract_time(input):
    time_regex = re.compile(r'^[1]?[0-9]:[0-5]?[0-9]$')  #145:23 -> start with [1]? then [0-9] char -> 1 digit, or 2 digit
    # time_regex = re.compile(r'[1]?[0-9]:[0-5]?[0-9]')  #("145:23")-> not working!
    # time_regex = re.compile(r'^\d\d?:\d\d$')
    match = time_regex.search(input)
    if match:
        return match.group()
    return None

def is_valid_time(input):
    time_regex = re.compile(r'^[1]?[0-9]:[0-5]?[0-9]$')  #("145:23")-> not working!
    # time_regex = re.compile(r'^\d\d?:\d\d$')
    match = time_regex.search(input)
    if match:
        return True
    return False

print(is_valid_time("10:45"))
print(is_valid_time("1:23"))
print(is_valid_time("10.45"))
print(is_valid_time("1999"))
print(is_valid_time("145:23"))
print(is_valid_time("98:45"))  #error in terms of time limmit of 12:59
