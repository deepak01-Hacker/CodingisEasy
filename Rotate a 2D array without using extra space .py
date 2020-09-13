#Python3

"""
    Code By    : Deepak Kumar
    Contact us : a9694060356@gmail.com

"""

#Problem : You are given an N x N 2D matrix Arr representing an image. 
#          Rotate the image by 90 degrees (clockwise). You need to do this 
#          in place. Note that if you end up using an additional array, you 
#          will only receive partial score.



//Explanation : 
"""
    Input:
    N = 3
    Arr[][] = {{1,  2,  3}
            {4,  5,  6}
            {7,  8,  9}}
    Output:
    3  6  9 
    2  5  8 
    1  4  7 
    Explanation: The given matrix is rotated
    by 90 degree in anti-clockwise direction.
"""



#ANswer of anticlock Wise Rotatio 90'
def rotateAntiClock(arr,n):
    for i in range(0,n//2):                     
        for j in range(i,n-i-1):
            temp = arr[i][j]
            arr[i][j] = arr[j][n-1-i]
            arr[j][n-i-1] = arr[n-i-1][n-1-j]
            arr[n-i-1][n-1-j] = arr[n-j-1][i]
            arr[n-j-1][i] = temp






    """
    3 6 9
    2 5 8
    1 4 7
    """

#Transpose of any 2d Array


def rota(arr,n):
    row = 0
    for i in range(n):
        for j in range(n):
            if j > i:
                t = arr[j][i]
                arr[j][i] = arr[i][j]
                arr[i][j] = t
    print(*arr)
    #if you reverse all rows then its is answer of clock wise 90'
 
    	        
if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        arr_in = list(map(int,input().rstrip().split(" ")))
        arr = [[ arr_in[i+j] for i in range(n)] for j in range(n)] 
        rotateAntiClock(arr,4)
        print(arr)

