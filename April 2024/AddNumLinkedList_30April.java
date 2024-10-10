/* node for linked list
class Node {
    int data;
    Node next;

    Node(int d) {
        data = d;
        next = null;
    }
}
*/
class Solution {
  // Function to add two numbers represented by linked list.
  static Node addTwoLists(Node num1, Node num2) {
    // Reverse the input lists
    Node n1 = reverse(num1);
    Node n2 = reverse(num2);
    int carry = 0;
    Node finalHead = null;

    // Loop through both lists until the end of both
    while (n1 != null || n2 != null || carry != 0) {
      int sum = carry;
      if (n1 != null) {
        sum += n1.data;
        n1 = n1.next;
      }
      if (n2 != null) {
        sum += n2.data;
        n2 = n2.next;
      }

      carry = sum / 10;
      Node newNode = new Node(sum % 10);
      newNode.next = finalHead;
      finalHead = newNode;
    }

    // Remove leading zeros
    while (finalHead != null && finalHead.data == 0) {
      finalHead = finalHead.next;
    }

    // If all nodes are zeros, we should return a single zero node
    if (finalHead == null) {
      return new Node(0);
    }

    return finalHead;
  }

  // Utility function to reverse the linked list
  private static Node reverse(Node head) {
    Node prev = null;
    Node current = head;
    Node next = null;

    while (current != null) {
      next = current.next;
      current.next = prev;
      prev = current;
      current = next;
    }

    return prev;
  }
}