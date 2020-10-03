#Python3

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
        n = int(input())
        arr = list(map(int,input().rstrip().split(" ")))
        print(matrixMultiplication(arr,1,n-1))
