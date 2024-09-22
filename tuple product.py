print('\033c')
tup1 = (4, 3, 2, 2, -1, 18)
tup2 = (2, 4, 8, 8, 3, 2)

newTup = ()

for i in range(0,len(tup1)):
    x = tup1[i] * tup2[i]
    newTup = newTup + (x,)
    
    
print(newTup)