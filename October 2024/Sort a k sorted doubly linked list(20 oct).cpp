class Solution {
  public:
    DLLNode *sortAKSortedDLL(DLLNode *head, int k) {
        //CodeGenius
        priority_queue<int,vector<int>,greater<int>>minHeap;
        DLLNode *temp1=head;
        DLLNode *temp2=head;
        while(temp1){
            minHeap.push(temp1->data);
            if(minHeap.size()==k+1){
                temp2->data=minHeap.top();
                minHeap.pop();
                temp2=temp2->next;
            }
            temp1=temp1->next;
        }
        while(!minHeap.empty()){
            temp2->data=minHeap.top();
            temp2=temp2->next;
            minHeap.pop();
        }
        return head;
    }
};
