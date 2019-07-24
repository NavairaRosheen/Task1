list=[1,2,5,-1,6,0,15]
smallest=min(list)
mini=list[0]
for i in list:
    if (i<mini) and (i>smallest):
        mini=i
print(mini)