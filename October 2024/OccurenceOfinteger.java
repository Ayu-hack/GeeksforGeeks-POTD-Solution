import java.util.*;

class Node {
    int data;
    Node next;

    Node(int a) {
        data = a;
        next = null;
    }
}

class Solution {
    public int count(Node head, int key) {
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

public class OccurenceOfinteger {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Read the number of nodes in the linked list
        System.out.println("Enter number of nodes:");
        int n = sc.nextInt();
        Node head = new Node(sc.nextInt());  // First node
        Node tail = head;
        
        // Create the linked list
        for (int i = 1; i < n; i++) {
            tail.next = new Node(sc.nextInt());
            tail = tail.next;
        }
        
        // Read the key to count
        System.out.println("Enter key value:");
        int key = sc.nextInt();
        Solution ob = new Solution();
        
        // Output the count of occurrences of the key
        System.out.println("Output:");
        System.out.println(ob.count(head, key));
        
        sc.close();
    }
}
