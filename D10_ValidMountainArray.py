'''
Question Description :-
Valid Mountain Array

Given an array of integers arr, return true if and only if it is a valid mountain array.
Recall that arr is a mountain array if and only if:
    arr.length >= 3
    There exists some i with 0 < i < arr.length - 1 such that:
    arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
    arr[i] > arr[i + 1] > ... > arr[arr.length - 1]



<-------strictly Increasing-----><--strictly Decreasing-->
0       2       3       4       5       2       1       0 
                    Valid Mountain Array


<--strictly Increasing--->----------------------<--------strictly Decreasing-------->
0           2           3           3           5           2           1           0 
                            Invalid Mountain Array


Example 1:
    Input: arr = [2,1]
    Output: false

Example 2:
    Input: arr = [3,5,5]
    Output: false

Example 3:
    Input: arr = [0,3,2,1]
    Output: true
 

Constraints:
    1) 1 <= arr.length <= 104
    2) 0 <= arr[i] <= 104
'''
def validMountainArray(arr):
    
    peak = 0
    n = len(arr)
    while (peak+1) < n and arr[peak] < arr[peak+1]:
        peak += 1
        
    if peak == n-1 or peak == 0:
        return False
        
    print(peak)
    down = peak
    while (down+1) < n and arr[down] > arr[down+1]:
            down += 1
            
    if down != n-1:
        return False
        
    return True

print(validMountainArray([9,8,7,6,5,4,3,2,1,0]))
