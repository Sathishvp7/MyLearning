"""
Wale wrote on single paper all different possible tuples x, y, z such that 1 less than or equal to x, y, z less than or equal to n. 
Then he sorted them in one row in the following order. First, the tuples are sorted increasingly according to their sum, 
i.e., x plus y plus z. If two tuples have the same sum, then the tuple with smaller value of x is put first. 
If two tuples have the same sum and the same value of x, then tuple with smaller y is put first. 
You are given the value of n and asked to find kth tuple. If required tuple is x, y, z,
you have to return the value of x plus 2 into y plus 3 into z. Note, it is a given that value of k is in the range of 1, n power of 3. 
You will be given k as a string and you need to convert into value into long long integer.
"""
def find_kth_tuple(n, k_str):
    k = int(k_str)
    tuples = []

    for x in range(1, n+1):
        for y in range(1, n+1):
            for z in range(1, n+1):
                tuples.append((x, y, z))

    # Sort based on (x + y + z), then x, then y
    tuples.sort(key=lambda t: (t[0] + t[1] + t[2], t[0], t[1]))

    # 1-based index
    x, y, z = tuples[k - 1]

    return x + 2*y + 3*z

print(find_kth_tuple(2, "5"))  # Returns value for the 5th sorted tuple
