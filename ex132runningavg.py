'''
rAvg = running_average()
rAvg(10) # 10.0
rAvg(11) # 10.5
rAvg(12) # 11

rAvg2 = running_average()
rAvg2(1) # 1
rAvg2(3) # 2
'''

def running_average(a):
    def inner1(b):
        return (a+b)/2
    return inner1

rAvg = running_average(10)
print(rAvg(10)) # 10.0
print(rAvg(11)) # 10.5
print(rAvg(12)) # 11

print("------2nd rAvg----------")
rAvg2 = running_average(1)
print(rAvg2(1)) # 1
print(rAvg2(3)) # 2

print("---------test closures-----")
def outer(a):
    def inner(b):
        return a + b
    return inner #return inner function

print(outer(10)) #function outer.inner -> outer(10) -> inner(b) func with return 10 + b

result = outer(10) 

print(result(20)) # 30 -> apply argument 20 to inner f -> inner(20)

print("--------lec----------------------")
def running_average1():
    running_average.accumulator = 0
    running_average.size = 0
  
    def inner(number):
        running_average.accumulator += number
        running_average.size += 1
        return running_average.accumulator / running_average.size
    
    return inner