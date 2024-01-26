for i in range(1, 100+1):
    if(i%10==0):
        print(i, end="\n")
    else:
        print(i, end=",")
print('***********'*5)
for i in range(1, 100+1):
    print(i, end=",")
    if(i%10==0):
        print("\ba")
    
        