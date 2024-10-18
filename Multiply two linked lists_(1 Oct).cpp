class solution {
  public:
   

const int MOD = 1e9 + 7;


long long multiplyTwoLists(Node* first, Node* second) {
    long long num1 = 0, num2 = 0;

    while (first != nullptr) {
        num1 = (num1 * 10 + first->data) % MOD;
        first = first->next;
    }

    while (second != nullptr) {
        num2 = (num2 * 10 + second->data) % MOD;
        second = second->next;
    }

   
    return (num1 * num2) % MOD;
}
// Function to create a linked list from a vector of integers

};
