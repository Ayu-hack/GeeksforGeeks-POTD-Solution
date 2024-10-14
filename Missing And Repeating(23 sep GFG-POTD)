class Solution {
  public:
    vector<int> findTwoElement(vector<int> arr) {
    sort(arr.begin(),arr.end());
        int A=0,B;
        for(int i=1;i<arr.size();i++){
            if((arr[i]-arr[i-1])==0){
                B=arr[i];
               
            }
            if((arr[i]-arr[i-1])>1){
                A=arr[i-1]+1;
            }else if(arr[0]!=1){
                A=1;
            }
        }
        if(A==0){
            A=arr[arr.size()-1]+1;
        }
        vector<int>ans;
        ans.push_back(B);
        ans.push_back(A);
        return ans;
        
    }
};
