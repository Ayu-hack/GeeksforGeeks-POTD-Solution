'''
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''
class Solution:
    def sumOfLastN_Nodes(self, head, n):
        # Initialize two pointers
        first = head
        second = head
        
        # Move first pointer n steps ahead
        for i in range(n):
            first = first.next
        
        # Move both pointers until first reaches the end
        while first:
            first = first.next
            second = second.next
        
        # Calculate the sum of the last n nodes
        sum_n_nodes = 0
        while second:
            sum_n_nodes += second.data
            second = second.next
        
        return sum_n_nodes
