# this file modified to check fetch download
n = int(input('Enter a number: '))
a=[]
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end=' ')
        if j<i:
            print('+',end=' ')
        a.append(j)
    print('=',sum(a))
print()


    
        
