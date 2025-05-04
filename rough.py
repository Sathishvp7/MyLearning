# # check list contain three consecutive numbers numbers = [1,2,2,2,3,4] - True; numbers = [4,5,6] - False;
# #arr = list(map(int, input().split(',')))
# arr = [1,2,2,2,3,4]
# status = False
# i = 1
# j = arr[0]
# k = 0
# while i < len(arr):
#   if arr[i]==j:
#     k += 1
#     if k == 2:
#       if arr[i]==arr[i-1]==arr[i-2]:
#         status = True
#         break
#       else:
#         k = 1
#   j = arr[i]
#   i += 1
# print(f"{status}\n")


t = ['flower', 'flow', 'flight']

print(sorted(t,reverse=True,key=  lambda x: len(x)))

# in sorted we can give multiple sort condition based like Based on Value first and key
dicts = {'a': 100, 'b': 120, 'c': 110, 'd': 120, 'e': 100}
print(dicts)
# sort based on value 
#First based on value if value same based on key
dd = dict(sorted(dicts.items(),key= lambda x:(x[1],x[0]),reverse=False))
print(dd)