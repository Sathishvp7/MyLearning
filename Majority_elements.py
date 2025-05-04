# 169. Majority Element
"""Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2

"""


def majorityElement(nums):
    Majority_element = 0
    count = 0

    for i in nums:
        if count == 0:
            Majority_element = i
            count = 1
        elif Majority_element == i:
            count += 1
        else:
            count -= 1
    print('Majority number is', Majority_element)
    return Majority_element
    
# bayers-Morre theorem
nums = [2,2,1,1,1,2,2,1,1]
majorityElement(nums)

