/*
The structure of linked list is the following
struct Node
{
    string data;
    Node* next;

    Node(int x){
        data = x;
        next = NULL;
    }
};
*/
class Solution {
  public:
    bool compute(Node* head) {
        // Your code goes here
        string s = "";
        while(head != NULL) {
            s += head->data;
            head = head->next;
        }
        string tt = s;
        reverse(tt.begin(), tt.end());
        return tt == s;
    }
};