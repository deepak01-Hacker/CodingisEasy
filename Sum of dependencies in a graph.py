#Python3

"""
    Code By    : Deepak Kumar
    Contact us : a9649060356@gmail.com

"""
$TaGs : Graph , Basic , GFG

#Problem :- the no of vertices and edges of the graph. Then in the next line are E pairs u and v denoting an edge from u to v.

#Example :- 
"""
    Input:
        2
        4 4 
        0 2 0 3 1 3 2 3
        4 3 
        0 2 0 1 0 3
    Output:
        4
        3
"""


def main():
    for _ in range(int(input())):
        vertices,edges = map(int,input().split(" "))
        Graph = list(map(int,input().rstrip().split(" ")))
        print(edges) #LEGENDS :) ;)


# Full Implementaion of Graph with map and sum of Dependencies
if __name__ == "__main__":
    for _ in range(int(input())):
        n,m = map(int,input().split(" "))
        arr = list(map(int,input().rstrip().split(" ")))
        map = {}
        for i in range(0,len(arr),2):
            try:
                map[arr[i]].append(arr[i+1])
            except:
                map[arr[i]] = []
                map[arr[i]].append(arr[i+1])
        result = 0
        for vertices in map:
            result += len(vertices)
        print(vertices)