class Solution {
  public:
    int minSteps(int d) {
        // code here
        queue<int> q;
        q.push(0);
        int l = 1;
        while(true){
            int n = q.size();
            unordered_set<int> pushed;
            for(int i = 0; i < n; i++){
                auto f = q.front();
                q.pop();
                int a = f + l, b = f + (-1)*l;
                if(a == d or b == d){
                    return l;
                 }
                 if(!pushed.count(a)){
                    q.push(a);
                    pushed.insert(a);
                 }
                 if(!pushed.count(b)){
                    q.push(b);   
                    pushed.insert(b);
                }
            }
            l++;
        }
        return -1;
    }
};
