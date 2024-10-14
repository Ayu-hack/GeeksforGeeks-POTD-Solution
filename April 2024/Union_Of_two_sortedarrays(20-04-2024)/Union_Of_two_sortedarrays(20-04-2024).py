
class Solution:
    
    
    def findUnion(arr1,arr2,n,m):
        List=[]
        arr3=arr1 + arr2
        arr4=sorted(arr3)
        List.append(arr4[0])
        for i in range(1,len(arr4)):
            if arr4[i] not in List :
                List.append(arr4[i])
            
        print(List) 
        
    findUnion(arr1=[2,2,3,4,5],arr2=[1,1,2,3,4],n=5,m=5)
           


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n,m = map(int,input().strip().split())
        a = list(map(int,input().strip().split()))
        b = list(map(int,input().strip().split()))
        ob=Solution() 
        li = ob.findUnion(a,b,n,m)
        for val in li:
            print(val, end = ' ')
        print()
