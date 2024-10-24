class Solution {

    // Return the sum of last k nodes
    public int sumOfLastN_Nodes(Node head, int n) 
    {
        // write code here
        if (head == null || n <= 0) {
            return 0; 
        }

        int length = 0;
        Node temp = head;
        while (temp != null) {
            length++;
            temp = temp.next;
        }

        int start = length - n;
        if (start < 0) {
            return 0; 
        }

        int sum = 0;
        temp = head;
        for (int i = 0; i < length; i++) {
            if (i >= start) {
                sum += temp.data;
            }
            temp = temp.next;
        }

        return sum;
    }
}
