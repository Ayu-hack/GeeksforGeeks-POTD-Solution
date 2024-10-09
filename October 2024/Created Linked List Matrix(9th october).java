class Solution {
    static Node construct(int arr[][]) {

        // Add your code here.

        Node head = new Node(arr[0][0]);
        Node node = head;
        for (int row = 0; row < arr.length; row++) {
            Node curr = node;
            for (int col = 0; col < arr[0].length; col++) {
                if (col+1 < arr[0].length)
                curr.right = new Node(arr[row][col+1]);
                if (row+1 < arr.length)
                curr.down = new Node(arr[row+1][col]);
                curr = curr.right;
            }
            node = node.down;
        }
        return head;
    }
}
