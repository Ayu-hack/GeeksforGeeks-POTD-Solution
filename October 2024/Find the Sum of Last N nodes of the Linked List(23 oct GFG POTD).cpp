class Solution {
  public:
    /*Structure of the node of the linled list is as

    struct Node {
        int data;
        struct Node* next;

        Node(int x){
            data = x;
            next = NULL;
        }
    };
    */
    // your task is to complete this function
    // function should return sum of last n nodes
    int sumOfLastN_Nodes(struct Node* head, int n) {
        stack<Node*>st;
        Node* temp=head;
        while(temp!=NULL){
               st.push(temp);
               temp=temp->next;
        }
        
        long long sum=0;
        
        while(!st.empty() && n-- ){
                Node* curr=st.top();
                sum+=curr->data;
                st.pop();
        }
        
        return sum;
    }
};

