class Solution {
  public:
    void reverseArray(vector<int> &arr) {
        // CodeGenius
        int s=0;
        int e=arr.size()-1;
        while(s<e){
            swap(arr[s],arr[e]);
            s++;
            e--;
        }
    }
};
