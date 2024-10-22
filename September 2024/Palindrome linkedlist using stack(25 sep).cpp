bool isPalindrome(Node* head) {
    Node* currNode = head;

    // Declare a stack
    stack<int> s;

    // Push all elements of the list to the stack
    while (currNode != nullptr) {
        s.push(currNode->data);
        currNode = currNode->next;
    }

    // Iterate in the list again and check by
      // popping from the stack
    while (head != nullptr) {
      
        // Get the topmost element
        int c = s.top();
        s.pop();

        // Check if data is not same as popped element
        if (head->data != c) {
            return false;
        }

        // Move ahead
        head = head->next;
    }

    return true;
}