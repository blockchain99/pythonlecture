users = [
	{"username": "samuel", "tweets": ["I love cake", "I love pie", "hello world!"]},
	{"username": "katie", "tweets": ["I love my cat"]},
	{"username": "jeff", "tweets": [], "color": "purple"},
	{"username": "bob123", "tweets": [], "num": 10, "color": "teal"},
	{"username": "doggo_luvr", "tweets": ["dogs are the best", "I'm hungry"]},
	{"username": "guitar_gal", "tweets": []}
]
print(sorted(users, key = len))
print("-------- reverse-----")
print(list(reversed(users)))
## alist.reverse()
# alist[::-1]
#list(reversed(alist))
print("+++")
print(sorted(users, key=lambda x: x['username']))
print("---tweet length--")
print(sorted(users, key=lambda x: len(x['tweets'])))

print("=== max magnitude : fartest from zero==")
def max_magnitude(nums):
    return max(abs(num) for num in nums)

def sum_even_values(*args):
    return sum(arg for arg in args if arg % 2 == 0)
def sum_floats(*args):
    return sum(arg for arg in args if type(arg) == float)
