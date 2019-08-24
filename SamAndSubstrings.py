#!/usr/bin/env python
# coding: utf-8
def substrings(s):
    totalSum = int(s[0])
    dp = int(s[0])
    size = len(s) - 1
    i = 1
    
    while i <= size:
        dp = (dp*10) + ((i+1) * int(s[i]))
        totalSum += dp
        i = i + 1
        
    return totalSum % ((10**9) + 7)




