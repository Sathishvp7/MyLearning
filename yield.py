def count_up_to(max_value):
    count = 1
    while count <= max_value:
        print('yield Started')
        yield count
        print('yield Paused')
        count += 1

# Using the generator
# for number in count_up_to(5):
#     print('Executed',number)


# example 2

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Get the first 10 Fibonacci numbers
fib_gen = fibonacci()
for _ in range(10):
    print(next(fib_gen))

