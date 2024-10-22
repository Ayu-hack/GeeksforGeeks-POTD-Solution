
class Solution {
  public:
    // Function to count nodes of a linked list.
    int getCount(struct Node* head) {

        int count = 0;
        Node* temp = head;
        while(temp != NULL){
            count++;
            temp = temp->next;
        }
        
        return count;
    }
};

