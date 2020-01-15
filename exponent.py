def exponent(num, power=2):
    """ exponent(num, power) raises num to specified power.Power default is 2"""
    return num ** power

print(exponent(3, 4))
print(exponent(3))
print(exponent(7))

print(exponent.__doc__)