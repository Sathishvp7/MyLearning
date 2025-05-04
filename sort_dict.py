# Sample dictionary
data = {'b': 2, 'a': 5, 'c': 1}

# Sorting by values without `sorted`
sorted_by_values = {}
items = list(data.items())

# Manual bubble sort for values
for i in range(len(items)):
    for j in range(i + 1, len(items)):
        if items[i][1] > items[j][1]:
            items[i], items[j] = items[j], items[i]

# Construct the sorted dictionary
for key, value in items:
    sorted_by_values[key] = value

print("Sorted by values:", sorted_by_values)


# Sample dictionary
data = {'b': 2, 'a': 5, 'c': 1}

# Sorting by keys without `sorted`
sorted_by_values = {}
items = list(data.items())

# Manual bubble sort for values
for i in range(len(items)):
    for j in range(i + 1, len(items)):
        if items[i][0] > items[j][0]:
            items[i], items[j] = items[j], items[i]

# Construct the sorted dictionary
for key, value in items:
    sorted_by_values[key] = value

print("Sorted by keys:", sorted_by_values)


# Sorting a Dictionary by Keys and Resolving Ties by Values
data = {'b': 2, 'd': 2,'a': 5, 'c': 1}

# Sorting by keys and values without `sorted`
sorted_by_keys_and_values = {}
items = list(data.items())

# Manual bubble sort for keys first, then values
for i in range(len(items)):
    for j in range(i + 1, len(items)):
        if items[i][0] > items[j][0]:  # Compare keys
            items[i], items[j] = items[j], items[i]
        elif items[i][0] == items[j][0] and items[i][1] > items[j][1]:  # Resolve tie by values
            items[i], items[j] = items[j], items[i]

# Construct the sorted dictionary
for key, value in items:
    sorted_by_keys_and_values[key] = value

print("Sorted by keys and values:", sorted_by_keys_and_values)

# sort by values without sorted inbulit function -  Descending order

dict1 = {'a': 23, 'b': 13, 'c': 30, 'd': 10}

new_sorted_dict = {}
dict1_list = list(dict1.items())
#print(dict1_list)

for i in range(len(dict1_list)):
    for j in range(i+1,len(dict1_list)):
        if dict1_list[i][1] < dict1_list[j][1]:
            dict1_list[i],dict1_list[j] = dict1_list[j], dict1_list[i]
print('Sorted descending order',dict1_list)

for k,v in dict1_list:
    new_sorted_dict[k] = v

print(new_sorted_dict)

