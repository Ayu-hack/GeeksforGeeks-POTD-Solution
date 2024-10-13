class Solution {
  public:
    void deleteAlt(struct Node *head) {
        
        Node* prev = head;
        Node* curr = head;
        Node* newLL = head;
        
        while(curr != NULL && curr -> next != NULL){
            
            curr = curr -> next -> next;
            prev -> next = curr;
            prev = curr;
        }
        
        // Code here
    }
};
