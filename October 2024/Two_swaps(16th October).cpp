class Solution {
  public:
    bool checkSorted(vector<int> &arr) {
        // code here.
        int count=0;
        for(int i=0;i<arr.size();i++){
            if(arr[i]!=i+1){
                swap(arr[i],arr[arr[i]-1]);
                count++;
                i--;
            }
            if(count>2)return false;
        }
        return count==2|count==0;
    }
};