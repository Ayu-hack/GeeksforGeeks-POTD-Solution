class Solution {
  public:
    int minRepeats(string& s1, string& s2) {
        //CodeGenius
        string temp=s1;
        int count=1;
        while(s1.size()<s2.size()){
            s1=s1+temp;
            count++;
        }
        if(s1.find(s2)!=-1) return count;
        s1=s1+temp;
        count++;
        if(s1.find(s2)!=-1) return count;
        return -1;
    }
};
