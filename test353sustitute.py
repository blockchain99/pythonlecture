# \g for group, <number> for group number: \g<1> -> group number 1
# re.compile('section{ (?P<name> [^}]* ) }', re.VERBOSE)
# -> \1 , \g<1>, \g<name>

import re
text = "Last night Mrs. Daisy and Mr. white murdered Ms. Chow"

pattern = re.compile(r'(Mr.|Mrs.|Ms.) ([a-z])[a-z]+', re.I) #g 2 is first char
# pattern = re.compile(r'(Mr.|Mrs.|Ms.) [a-z]+', re.I)
result0 = pattern.sub("REDACTED", text)
result1 = pattern.sub("\g<1> REDACTED", text)
result2 = pattern.sub("REDACTED \g<1>", text)
result3 = pattern.sub("\g<1> \g<2>", text)
print(result0)
print(result1)
print(result2)
print(result3)
