#Python3

"""
    Code By    : Deepak Kumar
    Contact us : a9649060356@gmail.com
"""

#Problem :- Find the maximum Longest Common Subsequence in Given Two String :?
#TaGs : Dynamic Programming 

#Explanation :-
"""
    string 1 : abscjfdojs
    string 2 : kjfanabsc

    Output : 4
"""

def LCS(lengthStringFirst,lengthStringSecond,st1,st2):
    if lengthStringFirst == 0 or lengthStringSecond == 0:
        return 0
    elif st1[lengthStringFirst-1] == st2[lengthStringSecond-1]:
        return 1+LCS(lengthStringFirst-1,lengthStringSecond-1,st1,st2)
    else:
        return max(LCS(lengthStringFirst,lengthStringSecond-1,st1,st2),LCS(lengthStringFirst-1,lengthStringSecond,st1,st2))

if __name__ == "__main__":
    for _ in range(int(input())):
        String1 = input()
        String2 = input()
        print(LCS(len(String1),len(String2),String1,String2))#Function that REturns Longest Common Subsequence length ////


#Happy Coding:)