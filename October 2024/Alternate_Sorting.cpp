//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
class Solution {

  public:
    vector<int> alternateSort(vector<int>& arr) {
        // Your code goes here
        vector<int>v;
        for(int i=0;i<arr.size();i++){
            v.push_back(arr[i]);
        }
        sort(v.begin(),v.end());
        int first=0;
        int second =v.size()-1;
        int count=0;
        while(first<second){
            arr[count++]=v[second];
            arr[count++]=v[first];
            first++;
            second--;
        }
        if(first ==second){
            arr[count]=v[first];
        }
        return arr;
        
    }
};


//{ Driver Code Starts.

int main() {
    string ts;
    getline(cin, ts);
    int t = stoi(ts);
    while (t--) {
        vector<int> arr;
        string input;
        getline(cin, input);
        stringstream ss(input);
        int number;
        while (ss >> number) {
            arr.push_back(number);
        }
        Solution obj;
        vector<int> ans = obj.alternateSort(arr);
        for (int i = 0; i < ans.size(); i++) {
            cout << ans[i] << " ";
        }
        cout << endl;
        cout << "~" << endl;
    }
    return 0;
}

// } Driver Code Ends