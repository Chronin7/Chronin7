#how to use map
def add_1(num):
    return num+1
nums=[1,2,3,4,5,6,7,8,9,10]
nums=map(add_1,nums)
for x in nums:
    print(x)
#how to use lambda
nums=[1,2,3,4,5,6,7,8,9,10]
nums=map(lambda num: num+1,nums)
for x in nums:
    print(x)
nums=[1,2,3,4,5,6,7,8,9,10]
print(x for x in list(map(lambda num: num+1,nums)))
