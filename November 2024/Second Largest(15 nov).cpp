class Solution {
  public:
    // Function returns the second
    // largest elements
   int getSecondLargest(vector<int> &arr) {
        // Code Here
        int mx1=INT_MIN,mx2=INT_MIN;
        for(int x:arr){
            if(x>mx1){
                mx2=mx1;
                mx1=x;
            }
            else if(x>mx2 && x!=mx1)mx2=x;
        }
        return mx2!=INT_MIN?mx2:-1;
    }
};
