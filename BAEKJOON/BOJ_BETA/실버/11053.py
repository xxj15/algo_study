# 가장 긴 증가하는 부분 수열 
import sys
input = sys.stdin.readline

n = int(input())

A = arr = list(map(int, input().split()))

dp = [1]*n

for i in range(1, n):
    for j in range(i):
        if A[j]<A[i]:
            dp[i] = max(dp[i], dp[j]+1)


print(max(dp))