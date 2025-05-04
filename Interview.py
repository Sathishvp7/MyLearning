# Ideas2IT
# main_string = 'hello'*4

# print()

# pattern_string = 'll'

# Output = 2



def string_index(main_string,pattern_string):
    result = []
    all_index = []


    for i in range(0,len(main_string)):

        result.append(main_string[i: i+len(pattern_string)])

        if main_string[i: i+len(pattern_string)] == pattern_string:
            all_index.append(i)
    return all_index


main_string  = 'hello'*4
pattern_string = 'll'

output = string_index(main_string,pattern_string)
print('All_index ',output)
#print('Strarting_index',output[1])