"""
136. Single Number
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:

Input: nums = [2,2,1]
Output: 1
Example 2:

Input: nums = [4,1,2,1,2]
Output: 4
Example 3:

Input: nums = [1]
Output: 1

"""
# solution 1
from collections import defaultdict

hash_int = defaultdict(int)

nums = [4,1,2,1,2]

for i in nums:
    hash_int[i] = hash_int[i] +1

result = []
for key, val in hash_int.items():
    if val == 1:
        result.append(key)
print('without default dict', result[0])


# solution 2
# without default dict

nums = [4,1,2,1,2]

without_default_dict = {}

for i in nums:
    if i not in without_default_dict:
        without_default_dict[i] = 1
    else:
        without_default_dict[i] = without_default_dict[i] + 1

result = []
for key, val in without_default_dict.items():
    if val == 1:
        result.append(key)
print('without default dict', result[0])

# soluition 3 - Most optimial solution - 6ms (Excellent)

nums = [4,1,2,1,2]
result = 0
for i in nums:
    result = result ^i
print('Optimal solutions using XOR', result)

# solution 4 -  insert and pop. - runtime 1066ms

nums = [4,1,2,1,2]
result = []

for i in nums:
    if i not in result:
        result.append(i)
    else:
        result.remove(i)

print('Using insert and pop',result[0])





