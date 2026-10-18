def maxProfit(prices):
    N = len(prices)
    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            ans = max(ans, prices[j] - prices[i])
    return ans

prices = [7,1,5,3,6,4]
print(maxProfit(prices))

prices = [7,6,4,3,1]
print(maxProfit(prices))