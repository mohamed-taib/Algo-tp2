def swap(T, i, j):
    T[i], T[j] = T[j], T[i]


def tas(T, n, i):
    big = i  
    left = (i * 2) + 1  
    right = (i * 2) + 2  

    if left < n and T[left] > T[big]:
        big = left

    if right < n and T[right] > T[big]:
        big = right

    if big != i:
        swap(T, i, big)  
        tas(T, n, big)  


def tasmax(T):
    n = len(T)
    for i in range(n // 2 - 1, -1, -1):
        parent = (i - 1) // 2  # Compute the parent index

        # Compare the current node with its parent during the heapify process
        if parent >= 0 and T[parent] < T[i]:  
            swap(T, parent, i)

        # Heapify the subtree rooted at the current node
        tas(T, n, i)


# Example array
T = [10, 22, 5, 18, 20, 25, 40, 30, 35, 12]
print("Original array:", T)

tasmax(T)
print("Max heap:", T)

