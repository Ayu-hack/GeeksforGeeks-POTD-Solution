vector<int> max_of_subarrays(int k, vector<int> &arr) {
        
        deque<int> dq;
        vector<int> ans;
        
        int n = arr.size();
        
        for(int i = 0; i < k; i++){
            
            while(!dq.empty() && arr[i] >= arr[dq.back()]){
                
                dq.pop_back();
            }
            dq.push_back(i);
        }
        // ans.push_back(dq.front());
        
        for(int i = k; i < n; i++){
            
            ans.push_back(arr[dq.front()]);
            
            while(!dq.empty() && dq.front() <= i-k){
                
                dq.pop_front();
            }
            
            while(!dq.empty() && arr[i] >= arr[dq.back()]){
                
                dq.pop_back();
            }
            dq.push_back(i);
            
        }
        if(!dq.empty()){
            
            ans.push_back(arr[dq.front()]);
        }
        
        
        return ans;
        // your code here
    }
};