class Solution 
{  
  public:    
  int minValue(Node* root) {       
    // Code here        
    Node* curr=root;        
    while (curr -> left != NULL){
      curr=curr->left;       
    }        
    return curr->data;   
}
