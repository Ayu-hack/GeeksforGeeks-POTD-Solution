
class Solution {
  public:
    vector<int> modifyAndRearrangeArray(vector<int> &a) {
        // Complete the function
            vector<int>ans(a.size());
        int j=0;
       for(int i=0;i<a.size()-1;i++){
           
           if(a[i]==0)continue;
           if(a[i]!=a[i+1]){ans[j++]=a[i];continue;}
         
           a[i]*=2;
           ans[j++]=a[i];
           a[i+1]=0;
       }
    ans[j]=a[a.size()-1];
       return ans;
    }
};
