
class Solution {
  public:
    // Function to count nodes of a linked list.
    int getCount(const struct Node* head) {
        int count = 0;
        const Node* temp = head;  // Use const to ensure no modification

        while (temp != nullptr) {  // Use nullptr for null pointer checks
            count++;
            temp = temp->next;
        }
        
        return count;
    }
};


