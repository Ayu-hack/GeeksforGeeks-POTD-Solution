
class Solution {
  public:
     int rotateDelete(vector<int> &arr) {
        int i = 1;
        int n = arr.size();
        while (i < (n / 2) + 1) {
            rotate(arr.begin(), arr.end() - 1, arr.end());
            arr.erase(arr.begin() + (arr.size() - i));
            i++;
        }
        return arr[0];
     }
};
