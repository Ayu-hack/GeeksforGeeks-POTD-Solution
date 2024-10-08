class Solution {
  public:
    void rearrange(vector<int> &arr) {
        
        
        // code here
        if(arr.size() > 1){
        vector<int> pos;
        vector<int> neg;
        
        for(int i = 0; i < arr.size(); i++){
            
            if(arr[i] < 0){
                
                neg.push_back(arr[i]);
            }
            else{
                
                pos.push_back(arr[i]);
            }
        }
        if(pos.empty() && !neg.empty()){
            
            arr = neg;
        }
        else if(neg.empty() && !pos.empty()){
            
            arr = pos;
        }
        else{
        arr.clear();
        int i = 0;
        int j = 0;
        
        while(!pos.empty() && !neg.empty() && i < pos.size() && j < neg.size()){
            
            arr.push_back(pos[i]);
            arr.push_back(neg[j]);
            i++;j++;
        }
        
        if(i <= pos.size()-1){
            
            while(i <= pos.size()-1){
                
                arr.push_back(pos[i]);
                i++;
            }
        }
        else if(j <= neg.size()-1){
            
            while(j <= neg.size()-1){
                
                arr.push_back(neg[j]);
                j++;
            }
        }
        }
        }
        
        
        
    }
};