def reverse_number(num):
    reversed_num = 0
    while num > 0:
        remainder = num % 10
        reversed_num = reversed_num * 10 + remainder
        num = num // 10
    return reversed_num

# Test the function
number = 12345
reversed_number = reverse_number(number)
print("Reversed number:", reversed_number)
