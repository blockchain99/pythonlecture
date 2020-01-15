import re
def censor(input):
    reg_ex = re.compile(r'frack[a-z]*',re.I)
    # reg_ex = re.compile(r'\bfrack\w*\b',re.I)  #\w : letter digit, _ #lec ver
    result = reg_ex.sub("CENSORED", input)
    return result

print(censor("Frack you"))
print(censor("I hope you fracking well"))
print(censor("you fracking Frack"))