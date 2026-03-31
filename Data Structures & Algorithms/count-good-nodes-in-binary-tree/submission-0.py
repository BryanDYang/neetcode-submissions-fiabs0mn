# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        gn = []
        maxNode = root.val

        def dfs(node: TreeNode, maxNode: int):

            if not node:
                return node, maxNode
            
            if node.val >= maxNode:
                gn.append(node.val)
                maxNode = node.val

            dfs(node.left, maxNode)
            dfs(node.right, maxNode)

        dfs(root, maxNode)

        return len(gn)

