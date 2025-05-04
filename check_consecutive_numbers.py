
# check list contain three consecutive numbers
# Method 1
def check_consecutive_numbers(numbers):
    answer = False
    for i in range(len(numbers)):
        count = numbers[i]
        repeat_count = 1
        for j in numbers[i+1:]:
            if j == count:
                repeat_count += 1
                if repeat_count == 3:
                    answer = True
                    return answer
            else:
                repeat_count -= 1
    return answer

# Method 2

numbers = [2,2,20,20,3,4] 
def check_consecutive_numbers_1(numbers):
    output = False
    for enu, i in enumerate(numbers[:-2]):
        my_list = numbers[enu: min(enu+3, len(numbers))]
        if len(set(my_list)) == 1:
            output =  True
            break

    return output
        
#numbers = [1,2,2,2,3,4] - True; [4,5,6] - False;
numbers = [1,2,3,2,3,3,4]
print('Method 1', check_consecutive_numbers(numbers))
print('Method 2',check_consecutive_numbers_1(numbers))