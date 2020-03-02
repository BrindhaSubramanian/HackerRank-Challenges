# Complete the kangaroo function below.

#Poor
def kangaroo1(x1, v1, x2, v2):
    n =1
    if x1<x2 and v1<v2:
        return "No"
    while(n<10000):
        print(x1+v1*n, x2+v2*n)
        if x1+v1*n == x2+v2*n:
            return 'Yes'
        n+=1
    return 'No'

#Better
def kangaroo(x1, v1, x2, v2):
    if x1<x2 and v1<v2:
        return "No"
    elif v1!=v2 and (x1-x2)%(v2-v1) == 0:
        return "Yes"
    else: return "NO"
