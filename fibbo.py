
# 0,1,1,2,3,5,8,13
def fibb(n):
    n1, n2 = 0,1
    res = [n1,n2]
    for i in range(2,n):
        n3 = n1 +n2
        res.append(n3)
        n1 = n2
        n2 = n3
    print(res)
    return res

fibb(n=10)


#



