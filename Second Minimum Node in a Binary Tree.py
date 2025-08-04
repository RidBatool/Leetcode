# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        result=[]
        def dfs(node, path):
            if not node:
                return 
            path.append(node.val)
            dfs(node.left, path)
            dfs(node.right, path)
        dfs(root, result)
        val= min(result)
        result.sort()
        for i in result:
            if i!=val:
                return i
        else:
            return -1
