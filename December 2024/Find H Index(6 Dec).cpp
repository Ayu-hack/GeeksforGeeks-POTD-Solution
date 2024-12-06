class Solution {
  public:
    int hIndex(vector<int>& citations) {
        //CodeGenius
        int n=citations.size();
        vector<int> freq(n+1);
        for(int i=0;i<n;i++){
            if(citations[i]>=n) freq[n]++;
            else freq[citations[i]]++;
        }
        int Hindex=n;
        int num=freq[n];
        while(num<Hindex){
            Hindex--;
            num+=freq[Hindex];
        }
        return Hindex;
    }
};
