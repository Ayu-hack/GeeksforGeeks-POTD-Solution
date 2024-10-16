def generate_fibonacci_series(N):
    if N==1:
        print(0)
    elif N==2:
        print (0,1,sep=" ",end=" ")
    else:
        f1=0
        f2=1
        print (0,1,sep=" ",end=" ")
        for i in range (N-2):
            f3=f1+f2
            print(f3,end=" ")
            f1,f2=f2,f3

N=int(input())
generate_fibonacci_series(N)
