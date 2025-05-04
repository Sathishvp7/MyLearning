# String Manipulation
# Reverse words in a string ("Hello World" -> "World Hello")

def reverse_word(s):
    reverse_word = ""
    tokens = [i for i in list(s.split(' '))]
    for i in range(1,len(tokens)+1):
        reverse_word = reverse_word + " "+ tokens[-i]
    print(reverse_word)
    return reverse_word

#reverse_word('Hello World life is wonder')

# Find the longest palindrome in a given string


def expand_around_center(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return s[left + 1:right]

def longest_palindrome(s):
    if not s or len(s) < 1:
        return ""

    longest = ""
    for i in range(len(s)):
        # Odd-length palindrome (single character center)
        odd_palindrome = expand_around_center(s, i, i)
        print(f'Odd {odd_palindrome}')
        if len(odd_palindrome) > len(longest):
            longest = odd_palindrome

        # Even-length palindrome (two character center)
        even_palindrome = expand_around_center(s, i, i + 1)
        print(f'even {even_palindrome}')
        if len(even_palindrome) > len(longest):
            longest = even_palindrome

    return longest

# Example Usage
s = "babad"
print(longest_palindrome(s))  # Output: "bab" or "aba"



