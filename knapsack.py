
def knapsack(w, p, c, n):
    dp = [[0]*(c+1) for i in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, c+1):
            if w[i-1] <= j:
                dp[i][j] = max(p[i-1] + dp[i-1][j-w[i-1]], dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]

    return dp[n][c]

w = [10, 20, 30]
p = [60, 100, 120]
c = 50
n = len(w)

print("Maximum profit:", knapsack(w, p, c, n))  