A = [-4, 3, 1, 0, 2, 5, 10, 8, 12, 9]

# Build Min Heap (Heapify)
# Time: O(N), Space: O(1)
import heapq
heapq.heapify(A)
print(A)


# Heap Push (Insert Element)
# Time: O(log n)
heapq.heappush(A, 4)
print(A)


# Heap Pop (Extract Minimum)
# Time: O(log n)
minn = heapq.heappop(A)
print(A, minn)


# Heap Sort
# Time: O(n log n), Space: O(N)
def heapsort(arr):
    heapq.heapify(arr)
    n = len(arr)

    new_list = [0] * n 

    for i in range(n):
        minn = heapq.heappop(arr)
        new_list[i] = minn
    
    return new_list

print(heapsort([1, 3, 5, 7, 9, 2, 3, 6, 8, 0]))


# Heap Push Pop: 
# Time: O(log n)
heapq.heappushpop(A, 99)
print(A)


###################################################################################################
B = [-4, 3, 1, 0, 2, 5, 10, 8, 12, 9]

# Building a Max Heap:
n = len(B)
# Negate all the values
for i in range(n):
    B[i] = -B[i]

heapq.heapify(B)
print(B)
largest = -heapq.heappop(B)
print(largest)

# Heap push to max heap
heapq.heappush(B, -7) # Inserts 7, not -7
print(B)


###################################################################################################
C = [-5, 4, 2, 1, 7, 0, 3]

# Build heap from scratch, without heapify
# Time: O(n log n)
heap = []

for i in C:
    heapq.heappush(heap, i)
    # print(heap, len(heap))


###################################################################################################
D = [5, 4, 3, 5, 4, 3, 5, 5, 4]

# Putting tuples of items on the heap
from collections import Counter

counter = Counter(D)
heap = []

for k, v in counter.items():
    heapq.heappush(heap, (v, k))

print(heap)
