#!/usr/bin/python3
""" Module for 0-minoperations"""


def minOperations(n):
    """Minimum Operations"""
    if n <= 1:
        return 0

    dp = [float("inf")] * (n + 1)
    dp[1] = 0

    for i in range(2, n + 1):
        j = 1
        while j * j <= i:
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + (i // j))
                if j != 1:
                    dp[i] = min(dp[i], dp[i // j] + j)
            j += 1

    return dp[n] if dp[n] != float("inf") else 0
