class Solution {
  public:
    int bs(vector<int>&ar, int l, int r, int k) {
        while(l <= r) {
            int mid = l + (r - l)/2;
            if(ar[mid] == k) return mid;
            else if(ar[mid] > k) r = mid - 1;
            else l = mid + 1;
        }
        return -1;
    }
    int search(vector<int>& ar, int key) {
        int n = ar.size();
        int l = 0, r = n-1;
        while(l < r) {
            int mid = l + (r - l)/2;
            if(ar[mid] < ar[r]) r = mid;
            else l = mid + 1;
        } 
        if(l == 0) return bs(ar, 0, n-1, key);
        else if(key >= ar[0] and ar[l-1] >= key) return bs(ar, 0, l-1, key);
        else return bs(ar, l, n-1, key);
    }
};