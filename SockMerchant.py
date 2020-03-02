# Initial Try
import math
def sockMerchant(n, ar):
    Dict = {}
    for i in ar:
        Dict[i] = ar.count(i)
    count = 0
    for i in Dict:
        if Dict[i] > 1:
            count = count + math.floor(Dict[i]/2)
    return count

sockMerchant(5,[1,1,3,4,9,9,9,9,10, 10, 10])

# Better solution with Counter
from collections import Counter
sock_count = Counter()
pairs = 0
ar = [1,1,3,4,9,9,9,9,10, 10, 10]
for sock in ar:
     if sock not in sock_count:
         sock_count[sock] += 1
     else:
         pairs += 1
         del sock_count[sock]  
print(pairs)
