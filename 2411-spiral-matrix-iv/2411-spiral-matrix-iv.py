# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix = [[-1 for _ in range(n)] for _ in range(m)]
        if not head:
            return matrix
        direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        currect_direction = 0
        x = 0
        y = 0
        x_add = direction[currect_direction][0]
        y_add = direction[currect_direction][1]

        while head:
            matrix[x][y] = head.val
            head = head.next
            x += x_add
            y += y_add

            if m <= x or x < 0 or n <= y or y < 0 or matrix[x][y] != -1:
                currect_direction = (currect_direction + 1) % 4
                x -= x_add
                y -= y_add
                x_add = direction[currect_direction][0]
                y_add = direction[currect_direction][1]
                x += x_add
                y += y_add
        return matrix