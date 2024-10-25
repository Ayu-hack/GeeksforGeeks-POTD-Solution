class Solution {

  public:
     vector<int> alternateSort(vector<int>& arr) {
         // Your code goes here
         vector<int>v;
         for(int i=0;i<arr.size();i++){
             v.push_back(arr[i]);
         }
         sort(v.begin(),v.end());
         int first=0;
         int second =v.size()-1;
         int count=0;
         while(first<second){
             arr[count++]=v[second];
             arr[count++]=v[first];
             first++;
             second--;
         }
         if(first ==second){
             arr[count]=v[first];
         }
         return arr;

     }
};
