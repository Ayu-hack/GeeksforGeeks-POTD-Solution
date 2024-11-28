class Solution {
  public:
    int myAtoi(char *s) {
        //CodeGenius
        int i=0, sign=1;
        long ans=0;
        
        while(s[i]==' ') i++;
        if(s[i]=='+'|| s[i]=='-'){
            sign=(s[i]=='-')?-1:1;
            i++;
        }
        while(s[i]>='0' && s[i]<='9'){
            ans=ans*10+(s[i]-'0');
            if(sign*ans>=INT_MAX) return INT_MAX;
            if(sign*ans<=INT_MIN) return INT_MIN;
            i++;
        }
        return (int)sign*ans;     
   }
};
