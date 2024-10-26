import java.util.Scanner;

public class OccurrenceOfinteger {
    
  /* static class Node {
        int data;
        Node next;

        Node(int a) {
            data = a;
            next = null;
        }
    }*/
  

    public static int count(Node head, int key) {
        int count = 0;
        Node temp = head;
        
        while (temp != null) {
            if (temp.data == key) {
                count++;
            }
            temp = temp.next;
        }
        
        return count;
    }

    /*public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Enter number of nodes:");
        int n = sc.nextInt();
        Node head = new Node(sc.nextInt()); 
        Node tail = head;
        
        for (int i = 1; i < n; i++) {
            tail.next = new Node(sc.nextInt());
            tail = tail.next;
        }
        
        System.out.println("Enter key value:");
        int key = sc.nextInt();
        
        System.out.println("Output:");
        System.out.println(count(head, key));
        
        sc.close();
    }*/
}
