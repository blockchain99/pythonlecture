import re
def parse_bytes(input):
    # byte_regex = re.compile(r'\b[01]{8}+\b') #multiple repeat at position 9-> error
    byte_regex = re.compile(r'\b[0-1]{8}\b')
    # byte_regex = re.compile(r'\b[01]{8}\b') #sane as above
    # byte_regex = re.compile(r'\b[0,1]{8}\b') #sane as above
    return byte_regex.findall(input) # return a list of all matches

print(parse_bytes("11010101 101 323"))
print(parse_bytes("my data is: 10101010 11100010"))
print(parse_bytes("asdsa"))

