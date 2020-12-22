'''
Question Description :-
Smallest Range II

Given an array A of integers, for each integer A[i] we need to choose either x = -K or x = K,
and add x to A[i] (only once).
After this process, we have some array B.
Return the smallest possible difference between the maximum value of B and the minimum value of B.

Example 1:
    Input: A = [1], K = 0
    Output: 0
    Explanation: B = [1]

Example 2:
    Input: A = [0,10], K = 2
    Output: 6
    Explanation: B = [2,8]

Example 3:
    Input: A = [1,3,6], K = 3
    Output: 3
    Explanation: B = [4,6,3]
 

Note:
    1) 1 <= A.length <= 10000
    2) 0 <= A[i] <= 10000
    3) 0 <= K <= 10000
'''
def smallestRangeII(A,K):
    
    n = len(A)
    A.sort()
    res = A[n-1] - A[0]

    for i in range(n-1):
        j = i+1
        low = min(A[0]+K,A[j]-K)
        high = max(A[n-1]-K,A[i]+K)

        res = min(res,high-low)

    return res


print(smallestRangeII([0,10],2))

#Reference :- https://www.youtube.com/watch?v=0nCEcim5e2A