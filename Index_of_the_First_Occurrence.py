"""
28. Find the Index of the First Occurrence in a String
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
"""


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        index_present = []

        for enu in list(range(len(haystack)- len(needle)+1)):
            compare  = haystack[enu:len(needle)+enu]
            if compare == needle:
                index_present.append(enu)
        if index_present:
            return index_present[0]
        else:
            return -1

        
haystack = "hello"
needle = "ll"



Solution().strStr(haystack,needle)



def str_str(haystack, needle):
    return haystack.find(needle)

# Test cases
print(str_str("sadbutsad", "sad"))   # Output: 0
print(str_str("leetcode", "leeto"))  # Output: -1
print(str_str("hello", "ll"))        # Output: 2
print(str_str("abc", "d"))           # Output: -1
