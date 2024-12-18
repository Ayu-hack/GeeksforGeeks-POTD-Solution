class Solution {
    static boolean isPossible(int arr[],int k,int mid){
        int sum=0,student=1;
        for(int x:arr){
            sum+=x;
            if(sum>mid){
                student++;
                sum=x;
            }
        }
        return student<=k;
    }
    public static int findPages(int[] arr, int k) {
        // code here
        if(k>arr.length)return -1;
        int sum = 0,mx=Integer.MIN_VALUE;
        for(int x:arr){
            sum+=x;
            mx=Math.max(mx,x);
        }
        int low=mx,high=sum,mid,ans=Integer.MAX_VALUE;
        while(low<=high){
            mid=(low+high)/2;
            if(isPossible(arr,k,mid)){
                high=mid-1;
                ans=Math.min(ans,mid);
            }
            else low=mid+1;
        }
        return ans;
    }
    
}
