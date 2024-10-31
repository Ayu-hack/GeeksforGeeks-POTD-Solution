//{ Driver Code Starts

#include <bits/stdc++.h>
using namespace std;

struct Node {
    char data;
    struct Node *next;

    Node(int x) {
        data = x;
        next = NULL;
    }
};

void printlist(Node *head) {
    if (head == NULL)
        return;
    while (head != NULL) {
        cout << head->data << " ";
        head = head->next;
    }
    cout << endl;
}

void append(struct Node **headRef, char data) {
    struct Node *new_node = new Node(data);
    struct Node *last = *headRef;

    if (*headRef == NULL) {
        *headRef = new_node;
        return;
    }
    while (last->next != NULL)
        last = last->next;
    last->next = new_node;
    return;
}


// } Driver Code Ends
/*
Structure of the node of the linked list is as
struct Node
{
    char data;
    struct Node *next;

    Node(char x){
        data = x;
        next = NULL;
    }

};
*/

class Solution {
  public:
    // Function to rearrange the linked list based on vowels
    struct Node *arrangeCV(Node *head) {
         // Set of vowels for quick lookup
        unordered_set<char> vowels = {'a', 'e', 'i', 'o', 'u'};

        // Pointers for separate vowel and consonant lists
        Node *vowelHead = nullptr, *vowelTail = nullptr;
        Node *consonantHead = nullptr, *consonantTail = nullptr;

        // Traverse the original list and split into vowel and consonant lists
        Node *current = head;
        while (current != nullptr) {
            if (vowels.count(current->data)) { // If current node is a vowel
                if (!vowelHead) {
                    vowelHead = vowelTail = current;
                } else {
                    vowelTail->next = current;
                    vowelTail = vowelTail->next;
                }
            } else { // If current node is a consonant
                if (!consonantHead) {
                    consonantHead = consonantTail = current;
                } else {
                    consonantTail->next = current;
                    consonantTail = consonantTail->next;
                }
            }
            current = current->next;
        }

        // Link the vowel list to the consonant list
        if (vowelTail) {
            vowelTail->next = consonantHead;
        }
        if (consonantTail) {
            consonantTail->next = nullptr;
        }

        // Return the head of the new list
        return vowelHead ? vowelHead : consonantHead;
    }
};


//{ Driver Code Starts.

// task is to complete this function
int main() {

    int T;
    cin >> T;
    cin.ignore();
    while (T--) {
        vector<char> arr;
        string input;
        getline(cin, input);
        stringstream ss(input);
        char number;
        while (ss >> number) {
            arr.push_back(number);
        }
        if (arr.empty()) {
            return NULL;
        }
        char val = arr[0];
        int size = arr.size();

        Node *head = new Node(val);
        Node *tail = head;

        for (int i = 1; i < size; i++) {
            val = arr[i];
            tail->next = new Node(val);
            tail = tail->next;
        }

        Solution obj;
        head = obj.arrangeCV(head);
        printlist(head);
        cout << "~" << endl;
    }
    return 0;
}

// } Driver Code Ends