class Solution {
  public:
    int kthMissing(vector<int> &arr, int k) {
        //CodeGenius
        int s=0;
        int e=arr.size()-1;
        while(s<=e){
            int mid=(s+e)/2;
            int missing=arr[mid]-mid-1;
            if(missing<k){
                s=mid+1;
            }
            else e=mid-1;
        }
        return k + s;
        
    }
};
