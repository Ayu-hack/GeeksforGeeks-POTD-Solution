class Solution {
  public:
    int peakElement(vector<int> &arr) {
        // Your code here
        if(arr.size() == 1){
            return 0;
        }
        if(arr[0] > arr[1]){
            return 0;
        }
        
        int n = arr.size();
        if(arr[n - 1] > arr[n - 2]){
            return n - 1;
        }
        
        for(int i = 1; i < n - 1; ++i){
            if(arr[i] > arr[i - 1] && arr[i] > arr[i + 1]){
                return i;
            }
        }
        return -1;
    }
    
};
