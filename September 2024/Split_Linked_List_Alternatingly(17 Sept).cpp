class Solution {
  public:
  
    Node* vecToNode(vector<int> v){
        
        Node* newLL = new Node(v[0]);
        Node* pointer_to_head = newLL;
        
        for(int i = 1; i < v.size(); i++){
            
            Node* temp = new Node(v[i]);
            pointer_to_head -> next = temp;
            pointer_to_head = temp;
        }
        return newLL;
    }
    // Function to split a linked list into two lists alternately
    vector<Node*> alternatingSplitList(struct Node* head) {
        
        Node* curr = head;
        int i = 1;
        vector<int> sub1;
        vector<int> sub2;
        
        while(curr != NULL){
            
            if(i % 2 != 0){
                
                sub1.push_back(curr -> data);
            }
            else{
                
                sub2.push_back(curr -> data);
            }
            i++;
            curr = curr -> next;
        }
        vector<Node*> ans;
        
        ans.push_back(vecToNode(sub1));
        ans.push_back(vecToNode(sub2));
        
        return ans;
        
        
        // Your code here
    }
};

