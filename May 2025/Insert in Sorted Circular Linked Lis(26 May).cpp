class Solution {
  public:
    Node* sortedInsert(Node* head, int data) {
        Node* n = new Node(data);
        if (!head) {
            n->next = n;
            return n;
        }
        Node* cur = head;
        while (true) {
            Node* nxt = cur->next;
            if ((cur->data <= data && data <= nxt->data) ||
                (cur->data > nxt->data && (data >= cur->data || data <= nxt->data)) ||
                nxt == head) {
                cur->next = n;
                n->next = nxt;
                if (data < head->data) head = n;
                break;
            }
            cur = nxt;
        }
        return head;
    }
};
