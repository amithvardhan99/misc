"""class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        p = nums
        p.sort()
        arr = []
        i = 0
        j = 1
        k = 2
        ctr = 0
        bo = True
        while True:
            su = p[i] + p[j] + p[k]
            if su == 0:
                arr.append([p[i],p[j],p[k]])
            #print(i,j,k)
            #print(su)
            #print()
            k += 1
            if k == len(p):
                j += 1
                k = j + 1
                if j == len(p) - 1:
                    i += 1
                    j = i + 1
                    k = i + 2
                    if i == len(p) - 2:
                        break
        if len(arr) <= 1:
            return arr
        
        i = 0
        j = 1
        ar = []
        ar.append(arr[0])
        while True:
            print(arr)
            if j == len(arr):
                break
            if ((arr[i][0] == arr[j][0]) and (arr[i][1] == arr[j][1]) and (arr[i][2] == arr[j][2])):
                #print(arr)
                del arr[j]
                if j == len(arr) - 1:
                    break
                else:
                    continue
            j += 1
            if j == len(arr):
                i += 1
                j = i + 1
                if i == len(arr) - 1:
                    break
        
        if len(arr) == 2:
            if arr[0][0] == arr[1][0] and arr[0][1] == arr[1][1] and arr[0][2] == arr[1][2]:
                arr = arr[0]
        return arr"""

import numpy as np
if __name__ == "__main__":
    print(np.array([1,2,3]))