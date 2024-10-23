
class Solution:
    def sumOfLastN_Nodes(self, head, n):
        current = head
        total_nodes = 0
        while current:
            total_nodes += 1
            current = current.next
        
        if n > total_nodes:
            return 0  
        current = head
        for _ in range(total_nodes - n):
            current = current.next
        
        sum = 0
        while current:
            sum += current.data
            current = current.next
        
        return sum





class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split('\n')

    t = int(data[0])
    for i in range(1, t + 1):
        arr = list(map(int, data[2 * i - 1].split()))
        n = int(data[2 * i])
        head = Node(arr[0])
        tail = head
        for value in arr[1:]:
            tail.next = Node(value)
            tail = tail.next
        ob = Solution()
        print(ob.sumOfLastN_Nodes(head, n))

