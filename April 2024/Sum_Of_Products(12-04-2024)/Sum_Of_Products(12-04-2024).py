# SUM OF PRODUCTS (12-04-2024)
class Solution:
    def pairAndSum( n, arr):
        List=[]
        for i in range(0,n):
            for j in range(i+1,n):
                  List.append(arr[i]&arr[j])
        
        print(sum(List))
                

    pairAndSum( n=3,arr= [5,10,15])


if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N=int(input())
        Arr=list(map(int,input().strip().split(' ')))
        ob=Solution()
        print(ob.pairAndSum(N,Arr))
