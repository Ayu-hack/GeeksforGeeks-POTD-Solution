class Solution {
  public:
    int countPairs(vector<int> &arr, int target) {
        //CodeGenius
        sort(arr.begin(),arr.end());
        int count=0,s=0,e=arr.size()-1;
        while(s<e){
            if(arr[s]+arr[e]>=target) e--;
            else{
                count+=e-s;
                s++;
            }
        }
        return count;
    }
};
