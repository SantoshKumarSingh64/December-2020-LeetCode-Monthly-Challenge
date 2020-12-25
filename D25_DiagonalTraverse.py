'''
Question Description :-
Diagonal Traverse

Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown in the below image.

 

Example:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

Output:  [1,2,4,7,5,3,6,8,9]

Note:
    The total number of elements of the given matrix will not exceed 10,000.
'''
def findDiagonalOrder(matrix):

    if not matrix:
        return []
    
    ans = []

    row = 0
    col = 0
    r  = len(matrix)-1
    c = len(matrix[0])-1
    
    while row <= r and  col <= c:

        while row > -1 and col <= c:
            ans.append(matrix[row][col])
            row -= 1
            col += 1
        row += 1
        col -= 1
        if col == c and row == 0:
            row += 1
        elif row == 0:
            col += 1
        else:
            row += 1

        while row <= r and col > -1:
            ans.append(matrix[row][col])
            row += 1
            col -= 1
        row -= 1
        col += 1

        if col == 0 and row == r:
            col += 1
        elif col == 0:
            row += 1
        else:
            col += 1

    return ans


print(findDiagonalOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16],[17,18,19,20],[21,22,23,24]]))