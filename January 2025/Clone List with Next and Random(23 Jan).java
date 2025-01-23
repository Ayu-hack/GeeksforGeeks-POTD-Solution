class Solution {
    // Function to clone a linked list with next and random pointer.
    Node cloneLinkedList(Node head) {
        // your code her
        // your code here
        Map<Node, Node> nodeMapping = new HashMap<>();
        
        // Dummy node to start building the cloned list
        Node dummyNode = new Node(0);
        Node currentOriginalNode = head;
        Node currentClonedNode = dummyNode;
        
        // Step 1: Create a clone of the linked list with only next pointers
        while (head != null) {
            Node clonedNode = new Node(head.data);
            currentClonedNode.next = clonedNode;
            nodeMapping.put(head, clonedNode);
            currentClonedNode = clonedNode;
            head = head.next;
        }
        
        // Step 2: Update the random pointers in the cloned list
        Node clonedHead = dummyNode.next; // Head of the cloned list
        while (currentOriginalNode != null) {
            if (currentOriginalNode.random != null) {
                clonedHead.random = nodeMapping.get(currentOriginalNode.random);
            }
            clonedHead = clonedHead.next;
            currentOriginalNode = currentOriginalNode.next;
        }
        
        return dummyNode.next;
    }
}
