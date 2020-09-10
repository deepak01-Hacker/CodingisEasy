#Python3
"""
    Code By     : Deepak Kumar
    Contact us  : a9649060356@gmail.com
"""


#Problem :-> using Frequency and heap print k maximum frequency element


import heapq

def kStream(arr,n):
    map = {}
    for i in arr:
        try:
            map[i] += 1
        except:
            map[i] = 1
    li = []
    for i in map:
        heapq.heappush(li,[map[i],i])
    print(li[-k:]) #if its not work then li[:-k]

if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int,input().rstrip().split()))
        k = int(input())
        kStream(arr,k)

#Happy Coding ; ) 
