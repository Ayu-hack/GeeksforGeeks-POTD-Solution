// User function Template for C++

/* Linked List node structure

struct Node {
    int data;
    struct Node *next;
};

*/

class Solution {
  public:
    Node* removeAllDuplicates(struct Node* head) {
        Node *temp = head;
        unordered_map<int, int> mp;
        while(temp != NULL) {
            mp[temp->data]++;
            temp = temp->next;
        }
        temp = head;
        Node *ans = new Node(NULL), *t3 = ans;
        while(temp != NULL) {
            if(mp[temp->data] == 1) {
                t3->next = new Node(temp->data);
                t3 = t3->next;
            }
            temp = temp->next;
        }
        return ans->next;
        
    }
};