#Python3

"""
    Code By     : Deepak Kumar
    Contact us  : a9649060356@gmail.com

"""
# Problem :-> Find Maximum profit of Fractional Knpasack ?

#Note : If you get maximum Values in this Space Then You have Profit 
#Hint : use Fraction

def maximumProfit(W,w_arr,v_arr):
    zip = []
    for i in range(int(len(v_arr))):
        zip.append((v_arr[i]/w_arr[i],v_arr[i],w_arr[i]))
    zip.sort(reverse=True)
    ans = 0
    for i in range(len(zip)):
        if zip[i][2] <= W:
            ans += zip[i][1]
            W -= zip[i][2]
        elif W < 0  or W == 0:
            break
        else:
            cap = W
            cap = cap *zip[i][0]
            ans += cap
            W = 0
    print(ans,zip)

if __name__ == "__main__":
    for _ in range(int(input())):
        Weight_KnapSack = int(input())
        Weight_arr = list(map(int,input().rstrip().split(" ")))
        Value_arr = list(map(int,input().rstrip().split(" ")))
        maximumProfit(Weight_KnapSack,Weight_arr,Value_arr)

#Happy Coding ;)