class Solution {
  public:
    int countNodesinLoop(Node *head) {
        if(head==NULL || head->next==NULL)
            return 0;
        Node* slow = head;
        Node* fast = head;
        slow = slow->next;
        fast = fast->next->next;
        while(fast && fast->next){
            if(slow == fast)
                break;
            slow = slow->next;
            fast = fast->next->next;
        }
        if(slow != fast)
            return 0;
        int ans = 0;
        slow = slow->next;
        ans++;
        while(slow != fast){
            slow = slow->next;
            ans++;
        }
        return ans;
    }
};
