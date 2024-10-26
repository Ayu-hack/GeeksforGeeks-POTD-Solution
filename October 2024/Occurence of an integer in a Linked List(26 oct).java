class Solution {
    public static int count(Node head, int key) {
         int count = 0;
         Node temp = head;

         // Traverse the linked list
         while (temp != null) {
             if (temp.data == key) {
                 count++;
             }
             temp = temp.next;
         }

         return count;
     }
    
}
