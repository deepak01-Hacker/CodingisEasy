#Python3

"""
    Code By    : Deepak Kumar
    Contact us : a9649060356@gmail.com

"""

#Problem :- Give the shortest string that contain sequence of Given Two String .
#TaGs : Dynamic Programming 

#Explanation :-
"""
    Input : 
        1
        abscjfdojs
        kjfanabsc
    Output : 
        LCS Length 4
        Super Common Sequence Length : 15
"""

def LCS(string1,string2,len_string1,len_string2):

    dp = [[0 for _ in range(len_string2+1)] for _ in range(len_string1+1)]

    for i in range(len_string1+1):
        for j in range(len_string2+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif string1[i-1] == string2[j-1]:
                dp[i][j] = 1+dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
    print("LCS Length "+str(dp[len_string1][len_string2]))
    start_ = len_string1
    last_ = len_string2
    ans_string = ""
    while(start_>0 and last_>0):
        if string1[start_-1] == string2[last_-1]:
            t = string1[start_-1]
            t += ans_string
            ans_string = t
            start_ -= 1
            last_ -= 1
        elif dp[start_-1][last_] > dp[start_][last_-1]:
            start_ -= 1
        else:
            last_ -= 1
    return ans_string

def shortestCommonSuperSequence(string1,string2,len_string1,len_string2):
    string_LCS = LCS(string1,string2,len_string1,len_string2)
    mergeString = string1+string2
    print("Super Common Sequence Length : "+str(len_string1+len_string2-len(string_LCS)))
    """string_LCS_pointer = 0
    superString = ""
    for i in range(len(mergeString)):
        if string_LCS_pointer < len(string_LCS) and string_LCS[string_LCS_pointer] == mergeString[i]:
            string_LCS_pointer += 1
        else:
            superString += mergeString[i]
    print(superString)"""
        

if __name__ == "__main__":
    for _ in range(int(input())):
        string1 = input()
        string2 = input()
        shortestCommonSuperSequence(string1,string2,len(string1),len(string2))