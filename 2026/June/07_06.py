# https://leetcode.com/problems/create-binary-tree-from-descriptions

# You are given a 2D integer array descriptions where descriptions[i] = [parenti, childi, isLefti]
# indicates that parenti is the parent of childi in a binary tree of unique values.

# Furthermore,
# If isLefti == 1, then childi is the left child of parenti.
# If isLefti == 0, then childi is the right child of parenti.
# Construct the binary tree described by descriptions and return its root.

# The test cases will be generated such that the binary tree is valid.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        parents, children = set(), set()
        nodes = {}

        def get_or_create( value):
            if value in nodes:
                return nodes[value]
            
            node = TreeNode(value)
            nodes[value] = node
            return node

        for parent, child, isLeft in descriptions:
            p_node = get_or_create(parent)
            if isLeft:
                p_node.left = get_or_create(child)
            else:
                p_node.right = get_or_create(child)
            parents.add(parent)
            children.add(child)

        for parent in list(parents):
            if parent not in children:
                return nodes[parent]

# <Medium>
# Runtime 167ms 34.96%
# Memory 28.07MB 27.44%
