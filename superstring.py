# https://app.programiz.pro/community-challenges/challenge/shortest-superstring/info#
"""Asuperstring of a set of strings is a single string that contains each

string in the set as a substring.
Let's take an example of a set of substrings, [ab, bc, ca].
The shortest possible superstring is abca as it contains all the substring 
[ab, bc, ca].

""" 

def shortest_superstring(strings):
    shortest_possible = strings[0]
    for i in strings[1:]:
        if i[0] == shortest_possible[-1:]:
            shortest_possible += i[1:]
        elif i[2:] == shortest_possible[-2:]:
            shortest_possible += i[2:]
        else:
            for j in i:
                if j not in shortest_possible:
                    shortest_possible+= j

    return shortest_possible

# ['a', 'b', 'c'] -- 'abc'
# ['abc', 'cde', 'efg'] -- 'abcdefg'
# ['xyz', 'yzx', 'zxy'] -- xyzxy
# ['cat', 'at', 'dog', 'og'] -- 'catdog'
inputs = ['cat', 'cat', 'dog', 'og']
print(shortest_superstring(inputs))
