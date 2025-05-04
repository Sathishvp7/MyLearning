# """
# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

# """
# class Solution(object):
#     def longestCommonPrefix(self, strs):
#         """
#         :type strs: List[str]
#         :rtype: str
#         """
#         my_inputs = []
#         match = False
#         final_result = ''
#         indexs = max(range(len(strs)), key=lambda i: len(strs[i]))
#         if len(strs) > 1:
#             for i in range(len(strs[indexs])):
#                 if i > 0:
#                     my_prefix = strs[0][:-i]
#                     my_inputs.append(my_prefix)
#                 else:
#                     my_prefix =strs[0][:]
#                     my_inputs.append(my_prefix)

#             for j in my_inputs:
#                 if len(final_result)==0:
#                     for k in strs[1:]:
#                         if j in k[:len(j)]:
#                             match = True
#                             final_result = j
#                         else:
#                             match = False
#                             final_result = ""
#                             break
#             return final_result
#         else:
#             return strs[0]

# strs = ["c","acc","ccc"]
# output = Solution().longestCommonPrefix(strs)
# print(output)


# second appoarch

def longest_common_prefix(strs):
    if not strs:
        return ""
    print('Before',strs)
    # Sort the array so the first and last strings will have the smallest common prefix
    strs.sort()
    print('After',strs)
    first, last = strs[0], strs[-1]

    i = 0
    while i < len(first) and i < len(last) and first[i] == last[i]:
        i += 1

    return first[:i]

# Example Usage:
print(longest_common_prefix(["flower","flow","flight"]))  # Output: "fl"
print(longest_common_prefix(["dog","racecar","car"]))     # Output: ""


#Alternative

def longest_common_prefix_vertical(strs):
    if not strs:
        return ""

    for i in range(len(strs[0])):  # Iterate through the characters of the first word
        char = strs[0][i]  # Take the character from the first string
        for string in strs[1:]:  # Compare with the rest of the strings
            if i >= len(string) or string[i] != char:  # If mismatch found
                return strs[0][:i]

    return strs[0]  # If all characters match completely

# Test cases
print(longest_common_prefix_vertical(["flower","flow","flight"]))  # Output: "fl"
print(longest_common_prefix_vertical(["dog","racecar","car"]))     # Output: ""
print(longest_common_prefix_vertical(["apple", "appetizer", "apply"]))  # Output: "app"
print(longest_common_prefix_vertical(["reboot", "rebound", "rebuild"])) # Output: "reb"
print(longest_common_prefix_vertical(["single"]))  # Output: "single"

