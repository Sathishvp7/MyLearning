# Group Anagrams
# Given a list of strings, group the words that are anagrams of each other.
# Input: ["eat", "tea", "tan", "ate", "nat", "bat"]  
# Output: [["eat","tea","ate"], ["tan","nat"], ["bat"]]


from collections import defaultdict

def group_anagrams(words):
    anagrams = defaultdict(list)
    
    for word in words:
        sorted_word = ''.join(sorted(word))  # Sort the characters in the word
        anagrams[sorted_word].append(word)
    
    return list(anagrams.values())

# Example usage:
words = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(words))

# Without Inbuilt function
# ananagram

words = ["eat", "tea", "tan", "ate", "nat", "bat"]

def group_anagram(words):
    output = {}
    for i in words:
        rearrange = "".join(sorted(i))
        if rearrange in output:
            output[rearrange].append(i)
        else:
            output[rearrange] = [i]
        print(rearrange)
    print(f'dict',output)
    print(f'dict_values',list(output.values()))
        
group_anagram(words)

## Find missing value
# Find the Missing Number in an Array
#Input: [3, 0, 1]  
#Output: 2  
inputs = [3,0,1]
missing_value = []

for i in range(min(inputs),max(inputs)+1):
    if i not in inputs:
        missing_value.append(i)
print(missing_value)



