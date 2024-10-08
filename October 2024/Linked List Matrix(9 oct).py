# Define the Node class for linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.down = None

# Function to construct the linked list matrix from a 2D array
def construct_linked_matrix(matrix):
    if not matrix or not matrix[0]:
        return None

    rows, cols = len(matrix), len(matrix[0])

    # Create a 2D array of nodes
    nodes = [[None for _ in range(cols)] for _ in range(rows)]

    # Initialize the linked list nodes
    for i in range(rows):
        for j in range(cols):
            nodes[i][j] = Node(matrix[i][j])

    # Set the right and down pointers
    for i in range(rows):
        for j in range(cols):
            if j + 1 < cols:
                nodes[i][j].right = nodes[i][j + 1]
            if i + 1 < rows:
                nodes[i][j].down = nodes[i + 1][j]

    # Return the head of the linked list matrix (top-left node)
    return nodes[0][0]

# Function to print the linked list matrix for verification
def print_linked_matrix(head):
    row_head = head
    while row_head:
        current = row_head
        while current:
            print(current.data, end=" ")
            current = current.right
        print()
        row_head = row_head.down

# Example matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Construct the linked list matrix and print it
head = construct_linked_matrix(matrix)
print_linked_matrix(head)
