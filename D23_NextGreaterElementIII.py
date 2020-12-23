'''
Question Description :-
Next Greater Element III

Given a positive integer n, find the smallest integer which has exactly the same digits existing in the integer n 
and is greater in value than n. If no such positive integer exists, return -1.
Note that the returned integer should fit in 32-bit integer, if there is a valid answer but it does not fit in 32-bit integer, 
return -1.

 
Example 1:
    Input: n = 12
    Output: 21

Example 2:
    Input: n = 21
    Output: -1
 
Constraints:
    1 <= n <= 231 - 1
'''
def nextGreaterElement(n):
    
    s = list(str(n))
    i = len(s)-1
        
                
    while i-1 >=0 and s[i-1] >= s[i]:
        i -= 1
            
    if i == 0: 
        return -1        
        
    j = len(s)-1
    while s[j] <= s[i-1]:
        j -= 1            
    
    s[i-1], s[j] = s[j], s[i-1]        
    s[i:] = s[i:][::-1]
    res = int(''.join(s))        
        
    if res <= 2**31-1:
        return res
    return -1

print(nextGreaterElement(101))
#Reference :- https://www.programmersought.com/article/93801160401/