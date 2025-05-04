def longest_unique_substring(s):
    char_set = set()
    left = 0
    max_length = 0
    start_index = 0
    longest_substring = ""

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
            print("".join(char_set))
            print('****')

        char_set.add(s[right])
        if right - left + 1 >= max_length:
            max_length = right - left + 1
            start_index = left
            print(longest_substring)
            longest_substring = s[start_index: right + 1]

    return longest_substring, max_length

# Example usage
s = "abccbcbb"
result, length = longest_unique_substring(s)
print(f"Longest unique substring: '{result}', Length: {length}")