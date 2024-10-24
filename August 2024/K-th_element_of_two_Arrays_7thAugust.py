class Solution:
    def kthElement(self, k, arr1, arr2):
        # If k is larger than total length of both arrays
        if k > len(arr1) + len(arr2):
            return -1
            
        # Simple solution using merge sort technique
        i, j = 0, 0  # Pointers for arr1 and arr2
        count = 0    # Count of elements processed
        last = 0     # Last element processed
        
        # Continue until we find kth element
        while i < len(arr1) and j < len(arr2):
            if arr1[i] <= arr2[j]:
                last = arr1[i]
                i += 1
            else:
                last = arr2[j]
                j += 1
            count += 1
            if count == k:
                return last
                
        # If elements in arr1 are remaining
        while i < len(arr1) and count < k:
            last = arr1[i]
            i += 1
            count += 1
            if count == k:
                return last
                
        # If elements in arr2 are remaining
        while j < len(arr2) and count < k:
            last = arr2[j]
            j += 1
            count += 1
            if count == k:
                return last
                
        return -1

def main():
    T = int(input())
    while (T > 0):
        k = int(input())
        a = [int(x) for x in input().strip().split()]
        b = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.kthElement(k, a, b))
        T -= 1

if __name__ == "__main__":
    main()
