/*
struct Job 
{ 
    int id;	 // Job Id 
    int dead; // Deadline of job 
    int profit; // Profit if job is over before or on deadline 
};
*/

class Solution 
{
    public:
    //Function to find the maximum profit and the number of jobs done.
    vector<int> JobScheduling(Job arr[], int n) 
    { 
        // your code here
        vector<pair<int, int>>ar;
        int mx = -1;
        for(int i=0; i<n; i++) {
            ar.push_back({arr[i].profit, arr[i].dead});
            mx= max(mx, arr[i].dead);
        }
        sort(ar.rbegin(), ar.rend());
        int profit = 0, cnt = 0;
        vector<int>cur(mx+1, -1);
        for(auto i:ar) {
            for(int j=i.second; j>0; j--) {
                if(cur[j] == -1) {
                    profit += i.first;
                    cur[j] = 1;
                    cnt++;
                    break;
                }
            }
        }
        return {cnt, profit};
    } 
};
