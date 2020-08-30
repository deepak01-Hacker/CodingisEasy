dp = [0] * 51
t = 0
def countn(n):
    global dp
    global t
    if n == 1 or n == 2 or n== 3:
        return 1
    elif n < 1:
        return 0
    elif dp[n]:
        return dp[n]
    dp[n] = (countn(n-1)+countn(n-2)+countn(n-5)+countn(n-1)*countn(n-2)*countn(n-3))
    return dp[n]
for _ in range(int(input())):
    n = int(input())
    print(countn(n,0))
    print(dp[:n])