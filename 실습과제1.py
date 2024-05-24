from itertools import combinations
import random

repeat = int(input('반복 횟수 : '))
nums = []

while True:
    if len(nums) == repeat:
        break
    a = random.randint(1,1000)
    if a in nums:
        continue
    else:
        nums.append(a)

print(nums)

def is_prime(num):
    for i in range(2,num):
        if num % i == 0:
            return False
    else:
        return True

def solutions(nums):

    com = list(combinations(nums,3))
    res = 0

    for i in range(len(com)):
        num = sum(list(com[i]))
        if is_prime(num) == True:
            res += 1
        else:
            continue
        
    return res

print(solutions(nums),'개의 소수가 나옵니다')