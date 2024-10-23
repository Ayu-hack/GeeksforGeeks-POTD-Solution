#include <bits/stdc++.h>
using namespace std;

// Solution class with the insertAtBottom method for stack<int>
class Solution {
public:
    // Function to insert an element at the bottom of the stack
    stack<int> insertAtBottom(stack<int> st, int x) {
        if (st.empty()) {
            st.push(x);
            return st;
        }
        
        int temp = st.top();
        st.pop();
        st = insertAtBottom(st, x);
        st.push(temp);
        
        return st;
    }
};

// Driver code
int main() {
    int t;
    cin >> t;
    
    while (t--) {
        int n, x;
        cin >> n >> x;
        stack<int> st;
        
        for (int i = 0; i < n; i++) {
            int a;
            cin >> a;
            st.push(a);
        }
        
        Solution ob;
        stack<int> tmp = ob.insertAtBottom(st, x);
        vector<int> v;
        
        while (!tmp.empty()) {
            v.push_back(tmp.top());
            tmp.pop();
        }
        
        reverse(v.begin(), v.end());
        for (int i = 0; i < v.size(); i++) {
            cout << v[i];
            if (i != v.size() - 1) {
                cout << " ";
            }
        }
        cout << endl;
    }
    
    return 0;
}
