# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
            
        maxD = 1
        q = deque([[1, root]]) # [root lvl, node]

        while q:
            level, node = q.popleft()
            maxD = max(level, maxD)

            if node.left:
                q.append([level + 1, node.left])
            if node.right:
                q.append([level + 1, node.right])
        
        return maxD
