#iterable -> "hello"
#iterator -> iter("hello")

def func(value1):
    return value1 + "!"

def for_loop(iterable, func):
    iterator = iter(iterable)
    while True:
        try:
            thing = next(iterator)
        except StopIteration:
            break 
        else:
            func(thing)

print(for_loop("hello", func))

print("-----generator is iterator, multiple output, yield----")
def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1

print(count_up_to(6)) #return generator object -> iterator obj
print(list(count_up_to(6)))

print("---generator express (...) like list comprehension [..] --")

def sum_of_nums():
    total = 0
    num = 1
    # while True:
    while total < 12:
        total += num
        yield total
        num += 1

s = sum_of_nums() # another generator!
print(f"* list of generator : {list(s)}")

