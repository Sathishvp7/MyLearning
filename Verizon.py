# longest Unique Substring

inputs = 'abcabcbc'

def longest_substring_unique(inputs):
    left = 0
    unique_substring = ''
    char_set = set()
    max_substring = 0
    count =1
    
    for right in range(len(inputs)):
        while inputs[right] in char_set:
            char_set.remove(inputs[left])
            left+= 1
            
        
        char_set.add(inputs[right])
        if len(char_set)> max_substring:
            max_substring = len(char_set)
            unique_substring+= inputs[right]
            print(f'COUNT {count} -->{unique_substring,max_substring} ')
            count += 1
        else:
            
            print(f'ELSE -->{unique_substring + inputs[right]} ')
                  
    return unique_substring,max_substring

longest_substring_unique(inputs)