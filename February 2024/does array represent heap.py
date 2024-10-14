def isMaxHeap(arr, n):
    for i in range(n // 2): 
        left_child_index = 2 * i + 1
        right_child_index = 2 * i + 2
        
        if left_child_index < n and arr[i] < arr[left_child_index]:
            return False
        
        if right_child_index < n and arr[i] < arr[right_child_index]:
            return False
    return True
