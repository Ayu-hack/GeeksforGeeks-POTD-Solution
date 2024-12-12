class Solution {
  public:
    int firstOcc(vector<int>& arr, int target){
        int s=0,e=arr.size()-1;
        int ans=-1;
        while(s<=e){
            int mid=(s+e)/2;
            if(arr[mid]==target){
                ans=mid;
                e=mid-1;
            }
            else if(arr[mid]>target) e=mid-1;
            else s=mid+1;
        }
        return ans;
    }
    int lastOcc(vector<int>& arr, int target){
        int s=0,e=arr.size()-1;
        int ans=-1;
        while(s<=e){
            int mid=(s+e)/2;
            if(arr[mid]==target){
                ans=mid;
                s=mid+1;
            }
            else if(arr[mid]>target) e=mid-1;
            else s=mid+1;
        }
        return ans;
    }
    int countFreq(vector<int>& arr, int target) {
        //CodeGenius
        if(lastOcc(arr,target)==-1 && firstOcc(arr,target)==-1) return 0;
        return lastOcc(arr,target)-firstOcc(arr,target) +1;
        
    }
};
