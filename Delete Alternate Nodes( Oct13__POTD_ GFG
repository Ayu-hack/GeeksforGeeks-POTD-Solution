class Solution {
  public:
    void deleteAlt(Node *head) {
        if (!head) return;  // If the list is empty, nothing to delete
        
        Node* current = head;
        
        while (current != nullptr && current->next != nullptr) {
            Node* temp = current->next;  // The node to be deleted
            current->next = current->next->next;  // Skip the next node
            delete temp;  // Free the memory of the deleted node
            current = current->next;  // Move to the next valid node
        }
    }
    
    // Utility function to print the linked list
    void printList(Node* head) {
        while (head != nullptr) {
            cout << head->data << " ";
            head = head->next;
        }
        cout << endl;
    }
};
