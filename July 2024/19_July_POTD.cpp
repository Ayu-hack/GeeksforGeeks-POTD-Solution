// User function Template for C++
//  User function template for C++
 #include <ext/pb_ds/assoc_container.hpp>
 using namespace __gnu_pbds;
 
 #define indexed_set tree<int,null_type,less_equal<int>,rb_tree_tag, tree_order_statistics_node_update>

class Solution {
  public:
    vector<int> constructLowerArray(vector<int> &arr) {
        // code here
       indexed_set s;
       vector<int>ans(arr.size());
       for(int i=arr.size()-1; i>=0; i--) {
           s.insert(arr[i]);
           ans[i] = s.order_of_key(arr[i]);
       }
       return ans;
    }
};