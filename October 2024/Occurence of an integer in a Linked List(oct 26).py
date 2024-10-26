"""  
class Node:
    def __init__(self, data):
		self.data = data
		self.next = None
  This is method only submission.
  You only need to complete the method.
"""
class Solution:
    def count(self, head, key):
        count = 0
        current = head
        while current:
            if current.data == key:
                count += 1
            current = current.next
        return count
