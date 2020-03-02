def bonAppetit(bill, k, b):
    if sum(bill) == b*2:
        print(math.floor(b-((sum(bill)-bill[k])/2)))
    else: print('Bon Appetit')	
