lwr = int(input('Enter start range number: '))
upr = int(input('Enter end range number: '))
for i in range(lwr,upr+1):
    if i%2 !=0 and i%3 !=0 :
        print(i)
    
