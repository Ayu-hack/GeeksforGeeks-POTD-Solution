 int x=0;
        int y=0,n=s.size();
        map<char,int>mp;
        for(int i=0;i<n;i++){
            mp[s[i]]++;
        }
        
        for(auto it :mp){
          int z=it.first-'a';
            if((z+1)%2!=0&&it.second%2!=0){
                y++;
            }
            if((z+1)%2==0&&it.second%2==0){
                x++;
            }
        }
            if((x+y)%2==0){
                return "EVEN";
            }else{
                return "ODD";
            }
