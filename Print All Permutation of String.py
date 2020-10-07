#Python3

"""
    Code By    : Deepak Kumar
    Contact us : a9649060356@gmail.com

"""

#Problem :- Print All Permutation of String (BackTracking)

#EXample:-
"""
    Input :
        1
        3
        abc
    Output:
        abc
        acb
        bac
        bca
        cba
        cab
"""



def swap(string,a,b):
    temp = string[a]
    string[a] = string[b]
    string[b] = temp

def printPermutatioin(string,start,last):
    if start == last:
        print(''.join(string))
    for swapPointer in range(start,last+1):
        swap(string,start,swapPointer)
        printPermutatioin(string,start+1,last)
        swap(string,start,swapPointer)

if __name__ == "__main__":
    for _ in range(int(input())):
        length = int(input())
        string = input()
        printPermutatioin(list(string),0,length-1)