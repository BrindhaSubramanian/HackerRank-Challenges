import math
def repeatedString(s, n):
    if s.count('a') == 0:
        return 0
    elif(len(set(s))==1):
        return n
    else:
        if len(s)<n:
            return s.count('a') * math.floor(n/len(s)) +  s[:n%len(s)].count('a')
        else: return s[:n].count('a')
