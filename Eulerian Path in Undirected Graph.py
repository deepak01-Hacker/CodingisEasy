#python3 
"""
    Code By : Deepak Insan
    Contact us: a9649060356@gmail.com 
"""
#Ques - >  Eulerian Path in an Undirected Graph ?
    -
    -
-   -   -
  - - -
    -   
#Equelerian Have property if any edges repeat or any vertex have odd Numbers then It is not a equalerianGraph .

for _ in range(int(input())):
    n = int(input())
    odd = 0
    for _ in range(n):
        a = list(map(int,input().rstrip().split(" ")))
        c = a.count(1)
        if c%2 == 1:
            odd += 1
    if odd == 2 or odd == 0:
        print(1)
    else:
        print(0)

#Happy Coding ;) Are you Understand ;) BytheWay MeanWhile ;)
