for i in range(9):
    for j in range(10):
        if j==0 or j==9 or i==4 or i==3 and(j!=4 and j!=5) or i==5 and(j!=4 and j!=5) or j==1 and(i!=0 and i!=8) or j==8 and(i!=0 and i!=8) or j==2 and(i!=0 and i!=8 and i!=1 and i!=7) or j==7 and(i!=0 and i!=8 and i!=1 and i!=7):
            print('*',end=" ")
        else:
            print(end='  ')
    print()
