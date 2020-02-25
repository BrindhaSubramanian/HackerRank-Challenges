def countingValleys(n, s):
    valleys = 0
    sealevel = 0
    for i in s:
        if i == 'U':
            sealevel+=1
        if i == 'D':
            sealevel+=-1
        if sealevel==0 and i == 'U':
            valleys = valleys+1            
    return valleys
