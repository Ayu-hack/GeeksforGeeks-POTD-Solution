class Solution {
  public:
    // Function to find the majority elements in the array
    vector<int> findMajority(vector<int>& arr) {
        // Your code goes here.
        unordered_map<int,int> map;
        int n = arr.size() /3;
        for(int i:arr) map[i]++;
        arr.clear();
        for(auto i:map) if(i.second > n ) arr.push_back(i.first);
        if(arr.size() == 2  && arr[0] > arr[1]) swap(arr[0],arr[1]);
        return arr;
    }
};
