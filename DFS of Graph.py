#Python3 

"""
    Code By     : Deepak Kumar
    Conatact us : a9649060356@gmail.com

"""

#Problem :- Find The DFS Traversal OF Graph:




def dp(G,n):
    stack = []
    stack.append(0)
    visited = [False for _ in range(n)]
    flag = True
    while(stack):
        flag = True
        if visited[stack[-1]] == False:
            print(stack[-1],end=" ")
            visited[stack[-1]] = True
        for value in G[stack[-1]]:
            if visited[value] == False:
                print(value,end=" ")
                stack.append(value)
                visited[value] = True
                flag = False
                break
        if flag:
            stack.pop()
    return []
    





#Ans : 0 3 5 7 10 4 1 13 11 14 12 2 9 6 8


#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)

#Contributed by : Nagendra Jha

#Graph Class:
class Graph():
    def __init__(self,vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def addEdge(self,u,v): # add directed edge from u to v.
        self.graph[u].append(v)

if __name__ == '__main__':
    test_cases = int(1)
    for cases in range(test_cases) :
        N,E = 15,19
        g = Graph(N)
        edges = [0 ,3 ,0, 4, 0 ,6 ,0, 8, 0, 13 ,1 ,4, 1 ,13 ,2 ,12 ,3 ,5 ,3 ,11, 3 ,13, 4 ,10 ,5 ,7, 5 ,10 ,5 ,12, 5, 13, 9, 12, 10 ,11 ,10 ,14]

        for i in range(0,len(edges),2):
            u,v = edges[i],edges[i+1]
            g.addEdge(u,v) # add an undirected edge from u to v
            g.addEdge(v,u)

        res = dp(g.graph,N)
        for i in range (len (res)):
            print (res[i], end = " ")
        print()
