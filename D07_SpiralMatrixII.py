'''
Question Description :-
Spiral Matrix II 

Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.


Example 1:
      ----------------------  
     |   1  |   2   |   3   |
      ----------------------
     |   8  |   9   |   4   |
      ----------------------
     |   7  |   6   |   5   |
      ----------------------
    Input: n = 3
    Output: [[1,2,3],[8,9,4],[7,6,5]]

Example 2:
    Input: n = 1
    Output: [[1]]
 
Constraints:
        1 <= n <= 20
'''
def generateMatrix(n):
        
    left,up = 0,0
    right,down = n-1,n-1
    
    case = 0
    ans = [[0 for x in range(n)]for y in range(n)]
    count = 1
        
    while left <= right and up <= down:
        
        if case == 0:
            for x in range(left,right+1):
                ans[up][x] = count
                count += 1
            up +=1
            
        elif case == 1:
            for x in range(up,down+1):
                ans[x][right] = count
                count += 1
            right -= 1
            
        elif case == 2:
            for x in range(right,left-1,-1):
                ans[down][x] = count
                count += 1
            down -= 1
            
        else:
            for x in range(down,up-1,-1):
                ans[x][left] = count
                count += 1
            left += 1
        
        case  = (case+1)%4
    
    return ans

print(generateMatrix(5))