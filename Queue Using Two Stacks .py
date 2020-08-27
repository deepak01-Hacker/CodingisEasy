"""
Code by : Deepak Kumar
contact us: a9649060356@gmail.com  
"""
#Question : Use Stack as a Queue:
#HackerRank : Medium Level 
#GeeksForGeeks : Easy Level

import os

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    stack = []
    res = []
    for _ in range(int(input())):
        operation = list(input().split(" "))
        if operation[0] == "1":
            stack.append(int(operation[1]))
        elif operation[0] == "2":
            stack.pop(0) # Main algo is here pop(0) is a inbuilt fn but in c , c++ you reverse element of stack and copy it in second after pop() the element and again copy in original 
        elif operation[0] == "3":
            res.append(stack[0])
        


    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()