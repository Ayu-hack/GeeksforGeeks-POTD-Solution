class Solution {
  public:
    void sort012(vector<int>& arr) {
        //CodeGenius
        int zeros=0,ones=0;
        for(int i=0;i<arr.size();i++){
            if(arr[i]==0) zeros++;
            else if(arr[i]==1)ones++;
        }
        for(int i=0;i<arr.size();i++){
            if(zeros){
                arr[i]=0;
                zeros--;
            }
            else if(ones){
                arr[i]=1;
                ones--;
            }
            else arr[i]=2;
        }
    }
};
