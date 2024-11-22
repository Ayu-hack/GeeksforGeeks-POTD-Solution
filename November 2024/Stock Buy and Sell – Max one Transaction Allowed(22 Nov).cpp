class Solution {
  public:
    int maximumProfit(vector<int> &prices) {
        //CodeGenius
        int maxele=0,maxProfit=0;
        for(int i=prices.size()-1;i>=0;i--){
            maxele=max(maxele,prices[i]);
            maxProfit=max(maxProfit,maxele-prices[i]);
        }
        return maxProfit;
    }
};
