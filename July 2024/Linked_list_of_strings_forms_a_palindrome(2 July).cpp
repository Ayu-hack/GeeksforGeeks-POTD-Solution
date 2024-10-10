class Solution {
  public:
    bool compute(Node* head) {
        
        string res = "";
        
        while(head != NULL){
            
            res += head -> data;
            head = head -> next;
        }
        string gg = res;
        
        reverse(res.begin(), res.end());
        
        if(res == gg){
            return true;
        }
        return false;
        // Your code goes here
    }
};



