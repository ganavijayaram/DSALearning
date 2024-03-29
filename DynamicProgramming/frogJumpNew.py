from os import *
from sys import *
from collections import *
from math import *

from typing import *

#Space optimisation
def frog3(arr, n, dp):
    first = 0
    if(n >= 1):
        second = abs(arr[0] - arr[1])

    for i in range(2, n):
        temp = min(second+abs(arr[i] - arr[i-1]), 
                first+abs(arr[i] - arr[i-2]))
        first = second
        second = temp
    return second

#TABULATION
def frog2(arr, n, dp):
    dp[0] = 0
    if(n >= 1):
        dp[1] = abs(arr[0] - arr[1])

    for i in range(2, n):
        dp[i] = min(dp[i-1]+abs(arr[i] - arr[i-1]), 
                dp[i-2]+abs(arr[i] - arr[i-2]))
    return dp[n-1]

#Memoization
def frog(arr, n, dp):
    if(n == 0):
        return 0
    if(dp[n] != -1):
        return dp[n]

    left = abs(arr[n] - arr[n-1]) + frog(arr, n-1, dp)
    right = maxsize
    if(n-2 >= 0):
        right = abs(arr[n] - arr[n-2]) + frog(arr, n-2, dp)
    dp[n] = min(left, right)
    #print(f"n {n} left {left} right {right} dp {dp}")
    return dp[n]


def frogJump(n: int, heights: List[int]) -> int:
    dp = [-1 for i in range(n)]
    return frog(heights, n-1, dp)
    
#Recursive solution
def rec(currStep, n, heights, minEnergy, currEnergy):
    if(currStep == n-1):
        if(minEnergy > currEnergy):
            minEnergy = currEnergy
        return minEnergy
    if(currStep > n):
        return minEnergy
    minEnergy = rec(currStep+1, n, heights, minEnergy,
                 currEnergy+abs(heights[currStep] - heights[currStep+1]))
    if(currStep+2 < n):
        minEnergy = rec(currStep+2, n, heights, minEnergy, 
                 currEnergy+abs(heights[currStep] - heights[currStep+2]))
    return minEnergy


def frogJump1(n, heights):
    #dp = [-1 for i in range(n+1)]
    print(f"Solution Recursive: {rec(0, n, heights, maxsize, 0)}")

height = [7, 4, 4, 2, 6, 6, 3, 4] 
print(f"Solution memo: {frogJump(len(height), height)}")

n = len(height)
dp = [-1 for i in range(n)]
print(f"Solution Tabulation: {frog2(height, n, dp)}")

n = len(height)
dp = [-1 for i in range(n)]
print(f"Solution Space Optimisation: {frog3(height, n, dp)}")
