'''
Question Description :-
Largest Rectangle in Histogram

Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, 
find the area of largest rectangle in the histogram.
                     6
                 5  ---
                ---|   |
               |   |   |     3
         2     |   |   | 2  ---
        ---  1 |   |   |---|   |  
       |   |---|   |   |   |   |
       |   |   |   |   |   |   |     
        -----------------------
Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].
The largest rectangle is shown in the shaded area, which has area = 10 unit.


Example:
    Input: [2,1,5,6,2,3]
    Output: 10
'''
def largestRectangleArea(heights):

    stack = [] 
    max_area = 0 
  
    index = 0
    while index < len(heights): 
          
        if (not stack) or (heights[stack[-1]] <= heights[index]): 
            stack.append(index) 
            index += 1
  
        else: 
            top_of_stack = stack.pop() 
            area = (heights[top_of_stack] * ((index - stack[-1] - 1) if stack else index)) 
            max_area = max(max_area, area) 
   
    while stack: 
           
        top_of_stack = stack.pop() 
        area = (heights[top_of_stack] * ((index - stack[-1] - 1) if stack else index))
        max_area = max(max_area, area)  
    
    return max_area 

print(largestRectangleArea([2,1,5,6,2,3]))

#Reference :- https://www.geeksforgeeks.org/largest-rectangle-under-histogram/