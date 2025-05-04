# Given an unsorted array of integers, find the length of the longest consecutive elements sequence in
# Input: [100, 4, 200, 1, 3, 2]  
# Output: 4  
# (Explanation: The longest consecutive sequence is [1, 2, 3, 4])  

def longest_consecutive(nums):
    num_set = set(nums)
    longest_streak = 0
    
    for num in num_set:
        if num - 1 not in num_set:  # Start of a sequence
            current_num = num
            current_streak = 1
            
            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1
            
            print(current_streak)
            longest_streak = max(longest_streak, current_streak)
    
    return longest_streak

# Example usage:
nums = [100, 4, 200, 1, 3, 2]
print(longest_consecutive(nums))  # Output: 4
