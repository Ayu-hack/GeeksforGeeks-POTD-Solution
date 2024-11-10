class Solution {
  public:
    // a,b : the arrays
    // Function to return a list containing the union of the two arrays.
    vector<int> findUnion(vector<int> &a, vector<int> &b) {
        // Your code here
        // return vector with correct order of elements
        int i=0,j=0,n=a.size(),m=b.size();
        vector<int> ans;
        while(i<n || j<m){
            int num1 = i<n?a[i]:INT_MAX;
            int num2 = j<m?b[j]:INT_MAX;
            if(num1<num2){
                ans.push_back(num1);
                i++;
            }
            else if(num2<num1){
                ans.push_back(num2);
                j++;
            }
            else{
                ans.push_back(num1);
                i++;
                j++;
            }
        }
        return ans;
    }
};
