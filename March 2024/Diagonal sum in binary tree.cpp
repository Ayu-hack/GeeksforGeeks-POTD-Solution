//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

struct Node {
    int data;
    struct Node* left;
    struct Node* right;
};

// Utility function to create a new Tree Node
Node* newNode(int val) {
    Node* temp = new Node;
    temp->data = val;
    temp->left = NULL;
    temp->right = NULL;

    return temp;
}

// Function to Build Tree
Node* buildTree(string str) {
    // Corner Case
    if (str.length() == 0 || str[0] == 'N')
        return NULL;

    // Creating vector of strings from input
    // string after spliting by space
    vector<string> ip;

    istringstream iss(str);
    for (string str; iss >> str;)
        ip.push_back(str);

    // Create the root of the tree
    Node* root = newNode(stoi(ip[0]));

    // Push the root to the queue
    queue<Node*> queue;
    queue.push(root);

    // Starting from the second element
    int i = 1;
    while (!queue.empty() && i < ip.size()) {

        // Get and remove the front of the queue
        Node* currNode = queue.front();
        queue.pop();

        // Get the current node's value from the string
        string currVal = ip[i];

        // If the left child is not null
        if (currVal != "N") {

            // Create the left child for the current node
            currNode->left = newNode(stoi(currVal));

            // Push it to the queue
            queue.push(currNode->left);
        }

        // For the right child
        i++;
        if (i >= ip.size())
            break;
        currVal = ip[i];

        // If the right child is not null
        if (currVal != "N") {

            // Create the right child for the current node
            currNode->right = newNode(stoi(currVal));

            // Push it to the queue
            queue.push(currNode->right);
        }
        i++;
    }

    return root;
}


// } Driver Code Ends
/*Complete the function below
Node is as follows:
struct Node{
    int data;
    Node *left,*right;
};
*/

class Solution {
  public:
    // root - root of the binary tree
    // vd - vertical distance diagonally
    // diagonalSum - map to store Diagonal
    // Sum(Passed by Reference)
    void diagonalSumUtil(struct Node* root, int vd, map<int, int>& diagonalSum) {
        if (!root)
            return;

        diagonalSum[vd] += root->data;

        // increase the vertical distance if left child
        diagonalSumUtil(root->left, vd + 1, diagonalSum);

        // vertical distance remains same for right child
        diagonalSumUtil(root->right, vd, diagonalSum);
    }

    // Function to calculate diagonal
    // sum of given binary tree
    vector<int> diagonalSum(struct Node* root) {
        vector<int> res;
        // create a map to store Diagonal Sum
        map<int, int> diagonalSum;

        diagonalSumUtil(root, 0, diagonalSum);

        map<int, int>::iterator it;

        for (it = diagonalSum.begin(); it != diagonalSum.end(); ++it) {
            res.push_back(it->second);
        }
        return res;
    }
};


//{ Driver Code Starts.

int main() {

    int t;
    scanf("%d ", &t);
    while (t--) {
        string s;
        getline(cin, s);
        Node* root = buildTree(s);
        Solution obj;
        vector<int> res = obj.diagonalSum(root);
        for (int i : res)
            cout << i << " ";
        cout << endl;
    }
    return 1;
}
// } Driver Code Ends
