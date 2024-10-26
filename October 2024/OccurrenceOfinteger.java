public class OccurrenceOfinteger {
    
  
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

    
}
