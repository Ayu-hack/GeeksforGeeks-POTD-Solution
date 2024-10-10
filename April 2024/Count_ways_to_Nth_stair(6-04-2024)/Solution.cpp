#include<bits/stdc++.h>
#include <vector>

class Solution {
  public:

    long long countWays(int n) {

        vector<int> v(n+1);
        v[0]=1;
        v[1]=1;

        
        for(int i=2; i<=n; i++){
            
            if(i%2 == 0){
                v[i]= v[i-1] + 1;    
            }
            else{
                v[i]=v[i-1];
            }
        }
        
        return v[n];
    }
};

