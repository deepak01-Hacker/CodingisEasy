#Python3

"""
    Code By    : Deepak Kumar
    Contact us : a9649060356@gmail.com

"""
#Problem :- Consider you have an infinite long binary tree having a pattern as below
#               1
#          2      3
#        4  5    6  7
#   .  .  .  .   .  .  .  . 

#You are given two nodes with values x and y, the task is to find the length of the shortest path between the two nodes.

#Example :
"""
    Input:
        2
        1 3
        2 2
    Output:
        1
        0

"""



#The Logic Behind The approach is :- the root = is odd or even its left child always contain Even and Right is Odd ; ) 

if __name__ == "__main__":
    for _ in range(int(input())):
        x,y = map(int,input().split(" "))
        check_root_Repeat = set()
        traverse_store = []
        while(x>0):
            traverse_store.append(x)
            check_root_Repeat.add(x)
            x = x//2
        result = 0
        index = 0
        while(y>0):
            if y in check_root_Repeat:
                index = y
                break
            result += 1
            y = y//2
        index = traverse_store.index(index)
        print(index+result)
        
            
