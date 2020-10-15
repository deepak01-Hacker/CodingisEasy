#Python3

"""
    Code By    : Deepak Kumar
    Contact us : a9649060356@gmail.com

"""

#Problem :- Given an array arr[] and a number K where K is smaller than size of array, the task is 
#           to find the Kth smallest element in the given array. It is given that all array elements are distinct.

#Example :- 
"""
    Input:
        2
        6
        7 10 4 3 20 15
        3
        5
        7 10 4 20 15
        4
    Output:
        7
        15

    Explanation:
        Testcase 1: 3rd smallest element in the given array is 7.
        Testcase 2: 4th smallest elemets in the given array is 15.
"""

class MaxHeap():
    def heappush(self, x): 
        heapq.heappush(self.h, MaxHeapObj(x))
    def heappop(self): 
        return heapq.heappop(self.h).val
    def __getitem__(self, i): 
        return self.h[i].val

import heapq

if __name__=="__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int,input().rstrip().split(" ")))
        k = int(input())
        heap = []
        heapq.heapify(heap)  
        for i in range(n):
            heapq.heappush(heap,-arr[i])
            if len(heap) > k:
                heapq.heappop(heap)
        t = heapq.heappop(heap)
        print(-t)