nums=[1,2,3,4,5,6]
print("-----------list comprehension------------")
nums1=[x*10 for x in nums]
print(nums1)
print([number * 100 for number in range(1, 5)])
print("--string converted from number--")
string_list = [str(num) for num in nums]
print(string_list)
print([bool(val) for val in [0, [], '', None, 1 ] ])
print("--- even ---")
evens = [nu % 2 == 0 for nu in nums]
print(evens)
evens1 = [ nu for nu in nums if nu % 2  == 0]
print(evens1)
print("------even : multiply by 2 odd: divide by 2---")
mul_div = [nu*2 if nu %2 == 0 else nu /2 for nu in nums]
print(mul_div)
print("===============join============")
words = ['Coding', 'Is', 'Fun!']
words1 = ' '.join(words) # 'Coding is Fun!'
print(words1)
name = ["Mr", "Steel"]
name2 = '. '.join(name)
print(name2)
print("=========for loop========")
nums2 = []
for n in nums:
    nums2.append(n*10)
print(nums2)    
print("========while loop======")
i = 0
nums3 = []
while i < len(nums):
    nums3.append(nums[i]*10)
    i += 1
print(nums3)
print("========map(lamda..)========")
map_obj = map(lambda x : x*10, nums)
print(map_obj)
print(list(map_obj))

print("======append ======")    
nums.append("500")
print(nums)
print("-----extend------")
nums.extend([100, 101, 102])
print(nums)
print("-------pop--------")
nums.pop()
print(nums)
nums.pop(1)
print(nums)
nums.insert(1, 2)
print(nums)
print("----------remove x -------")
nums.remove(4) #remove first element 4
print(nums)
print("insert-(positon, x)--------")
nums.insert(3,'Hi') # insert at index 3
print(nums)
nums.insert(4,'Hooo') # insert at index 4 
print(nums)
nums.insert(-1,'The end-1') #-1: before last(-1)
print(nums)
nums.insert(-2,'The end-2') #-2: before (-2)
print(nums)
print(nums[-1])

print("==========del nums[i] : deletes a nums[i] from a list")
del nums[3]
print(nums)
print("----returns the index of the specified item in the list")
print(nums.index('Hooo'))
print(nums.index(2,1))
print("+++++++++++++++++++++")
n2 = [5,5, 6,7,5,8,8, 9,10]
print(n2.index(5))  #index of the first duplicated element  -> 0
print(n2.index(5, 1)) # index of element 5 starting first-> 1
print(n2.index(5, 2)) # index of element 5 starting second -> 4
print(n2.index(8, 6, 8))
print("------count(x) : frequency of x")
print(n2.count(5))
print("`````````reverse```")
n2.reverse()
print(n2)
print("------ sort-----")
n2.sort()
print(n2)

print("============")
words=['coding', 'is', 'fun']
upper_words = []
for w in words:
    upper_words.append(w[0].upper()+w[1:])
print(upper_words)

upper_words1 = [x[0].upper() + x[1:] for x in words]
print(f"==list comprehension: first Capital=={upper_words1}")
print("--- list comprehension2 with list element ----")
upper_words11 = [x[0].upper()+x[1:] for x in words]
print(upper_words11)

upper_words1=[]
out = map(lambda x: x[0].upper()+x[1:], words)
print(out)
upper_words2 = list(out)
print(upper_words2)

print("---------slice: first index to sart scling from [1:]------------")
first_list = list(range(1, 5))
print(first_list)
sliced1 = first_list[1:] #from index1, after 0
print(sliced1)
print(first_list)
print(first_list[3:])
print(first_list[1:3]) #2 element, end not incl
print("======= [-1:] ======")
print(first_list[-1:])
print(first_list[-3:])
print("---------slice: second parameter for slice :end [:4]")
first_list = [1, 2, 3, 4]

print(first_list[:2]) # [1, 2]

print(first_list[:4]) # [1, 2, 3, 4] ####more than size of list!!!

print(first_list[1:3]) # [2, 3]
print(first_list[:])
print(first_list[:-1]) # [1, 2, 3]
print(first_list[1:-1]) # [2, 3]

print("-----slice with step----------------")
first_list = [1, 2, 3, 4, 5, 6]

print(first_list[::2])#odd
print(first_list[1::2]) #even
print("----[::-1]----")
print(first_list[1::-1]) # [2, 1]

print(first_list[:1:-1]) # [6, 5, 4, 3]

print(first_list[2::-1]) # [3, 2, 1]
print("--------- refversing lists/string-------")
string="This is fun!"
print(string[::-1])
print("-----------modifying the list")
numbers = [1,2,3,4,5]
#index size and to be inserted size can be defferent
numbers[1:3] = ['a','b','c'] 
print(numbers)

print("----clear---")
nums.clear()
print(nums)