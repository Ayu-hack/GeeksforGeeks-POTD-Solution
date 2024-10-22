class Solution:
    def delete_node(self, head, x):
        if not head:
            return None
        
        if x == 1:
            new_head = head.next
            if new_head:
                new_head.prev = None
            return new_head
        
        current = head
        count = 1
        
        while current and count < x:
            current = current.next
            count += 1
        
        if current:
            if current.next:
                current.next.prev = current.prev
            if current.prev:
                current.prev.next = current.next
        
        return head


class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None


def push(tail, new_data):
    newNode = Node(new_data)
    newNode.next = None
    newNode.prev = tail

    if tail:
        tail.next = newNode

    return newNode


def verifyDLL(head):
    c1, c2 = 0, 0
    tmp = head
    while tmp.next:
        c1 += 1
        tmp = tmp.next
    while tmp.prev:
        c2 += 1
        tmp = tmp.prev
    return c1 == c2


def printList(head):
    if not head:
        return
    if verifyDLL(head) == False:
        return
    while head:
        print(head.data, end=" ")
        head = head.next
    print()

#{ 
 # Driver Code Starts
class Node:

    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None


def push(tail, new_data):
    newNode = Node(new_data)
    newNode.next = None
    newNode.prev = tail

    if tail:
        tail.next = newNode

    return newNode


def verifyDLL(head):
    c1, c2 = 0, 0
    tmp = head
    while tmp.next:
        c1 += 1
        tmp = tmp.next
    while tmp.prev:
        c2 += 1
        tmp = tmp.prev
    return c1 == c2


def printList(head):
    if not head:
        return
    if verifyDLL(head) == False:
        return
    while head:
        print(head.data, end=" ")
        head = head.next
    print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))
        head = Node(arr[0])
        tail = head

        for value in arr[1:]:
            tail = push(tail, value)

        ob = Solution()
        resHead = ob.delete_node(head, int(input().strip()))
        printList(resHead)

# } Driver Code Ends
