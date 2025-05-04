# Sort the number without inbuilt functions

# Example - 1
# nums = [3,1,-1,2,-3,-2] --> Output = [-3,-2,-1,1,2,3]

#nums = [3,1,-1,2,-3,-2]
nums = [0,1,0,1,0,0,1,1,1,0,1,0,1,1,1,0]
len_n = len(nums)
for i in range(len_n):
    for enu,j in enumerate(range(len(nums)-1)):
        if nums[j] < nums[enu+1]:
            nums[j],nums[enu+1] = nums[enu+1] ,nums[j]
print('Sorted', nums)

# Problem 2 similar proble
# Name - Zeros and ones
# Description - Make sorting zeros and 1 (Ascending)
# Note this problem will work with above logic but O(2n)
# Now we try to find O(n)
"""
Check 1 and last index,
if first 0 move Right
if second 1 move Left
if second =1 and second = 0---> swap
"""

nums = [0,1,0,1,0,0,1,1,1,0,1,0,1,1,1,0]

def ZerosandOnes(new_list):
    n = len(new_list)
    first = 0
    second = n - 1
    print(first,second)
    while first < second:
        print(first,second)
        if new_list[first] == 0:
            first += 1
        if new_list[second] == 1:
            second -= 1
        if new_list[first] ==1 and new_list[second] ==0:
            new_list[first],new_list[second] = new_list[second],new_list[first]
    print('Sorted Zeros and ones ',new_list)

ZerosandOnes(nums)


sorted()