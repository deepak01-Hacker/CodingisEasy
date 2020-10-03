#Python3

"""
    Code By    : Deepak Kumar
    Contact Us : a9649060356@gmail.com
    GeeksForGeeks

"""
#Problem :- Given a sequence of matrices, find the most efficient way to multiply these matrices together. 
#           The problem is not actually to perform the multiplications, but merely to decide in which order to perform the multiplications.


#Example :
"""
    Input: p[] = {40, 20, 30, 10, 30}   
    Output: 26000  
    There are 4 matrices of dimensions 40x20, 20x30, 30x10 and 10x30.
    Let the input 4 matrices be A, B, C and D.  The minimum number of 
    multiplications are obtained by putting parenthesis in following way
    (A(BC))D --> 20*30*10 + 40*20*10 + 40*10*30

    Input: p[] = {10, 20, 30, 40, 30} 
    Output: 30000 
    There are 4 matrices of dimensions 10x20, 20x30, 30x40 and 40x30. 
    Let the input 4 matrices be A, B, C and D.  The minimum number of 
    multiplications are obtained by putting parenthesis in following way
    ((AB)C)D --> 10*20*30 + 10*30*40 + 10*40*30

    Input: p[] = {10, 20, 30}  
    Output: 6000  
    There are only two matrices of dimensions 10x20 and 20x30. So there 
    is only one way to multiply the matrices, cost of which is 10*20*30

"""



Mini = 10**5
def matrixMultiplication(arr,i,j):
    global Mini
    if i>=j:
        return 0
    for k in range(i,j):
        temp = matrixMultiplication(arr,i,k)+matrixMultiplication(arr,k+1,j)+(arr[i-1]*arr[k]*arr[j])
        Mini = min(Mini,temp)
    return Mini
    

if __name__ == "__main__":
    for _ in range(int(input())):
        Mini = 10**5
        n = int(input())
        arr = list(map(int,input().rstrip().split(" ")))
        print(matrixMultiplication(arr,1,n-1))
