# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result = []
        level = [root]
        while level:#keep going as long as there nodes on that level
            result.append([node.val for node in level])
            next_level =[] # build next level 
            for node in level:
                if node.left:
                    # if this node has a left child, add it to the next level
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            level = next_level

        return result 
        #input is a tree node 
        #output is a list of lists 
        #and you seperate by what?? 