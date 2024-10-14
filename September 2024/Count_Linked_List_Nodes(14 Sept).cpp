class Solution {
  public:
  
    int length(Node* head){
        
        int len = 0;
        Node* temp = head;
        
        while(temp){
            
            len++;
            temp = temp -> next;
            
        }
        return len;
    }
    // Function to count nodes of a linked list.
    int getCount(struct Node* head) {
        
        int ans = length(head);
        
        return ans;

        // Code here
    }
};
