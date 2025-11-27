#Given the root of a  BST with unique node values, transform it into greater sum tree where each node contains sum of all nodes greater than that node.

#Examples:

#Input: root = [11, 2, 29, 1, 7, 15, 40, N, N, N, N, N, N, 35, N]
      
#Output: [119, 137, 75, 139, 130, 104, 0, N, N, N, N, N, N, 40, N]
#Explanation: Every node is replaced with the sum of nodes greater than itself. 
      
#Input: root = [2, 1, 6, N, N, 3, 7]
     
#Output: [16, 18, 7, N, N, 13, 0]
#Explanation: Every node is replaced with the sum of nodes greater than itself. 
     
#Constraints :
#1 ≤ node->data ≤ 3*104
#1 ≤ number of nodes ≤ 3*104
#Expected Complexities
#Time Complexity: O(n)
#Auxiliary Space: O(n)

class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def transformTree(self, root):
        # Helper function to perform reverse in-order traversal
        def reverse_inorder(node, acc):
            if node is None:
                return acc
            
            # Traverse right subtree first (greater values)
            acc = reverse_inorder(node.right, acc)
            
            # Update current node value
            original_val = node.data
            node.data = acc
            acc += original_val
            
            # Traverse left subtree (smaller values)
            acc = reverse_inorder(node.left, acc)
            
            return acc
        
        # Start with accumulator = 0
        reverse_inorder(root, 0)
        return root
        
from collections import deque

def build_tree_from_list(values):
    """Build tree from level order list (like in examples)"""
    if not values:
        return None
    
    root = Node(values[0])
    queue = deque([root])
    i = 1
    
    while queue and i < len(values):
        node = queue.popleft()
        
        # Left child
        if i < len(values) and values[i] is not None:
            node.left = Node(values[i])
            queue.append(node.left)
        i += 1
        
        # Right child
        if i < len(values) and values[i] is not None:
            node.right = Node(values[i])
            queue.append(node.right)
        i += 1
    
    return root


def tree_to_list(root):
    """Convert binary tree to level order list (like in examples)"""
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        
        if node:
            result.append(node.data)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    
    # Remove trailing None values to clean up the list
    while result and result[-1] is None:
        result.pop()
    
    return result


def test_with_level_order():
    sol = Solution()
    
    # Test cases from the problem
    test_cases = [
        ([11, 2, 29, 1, 7, 15, 40, None, None, None, None, None, None, 35, None], [119, 137, 75, 139, 130, 104, 0, None, None, None, None, None, None, 40, None]),
        ([2, 1, 6, None, None, 3, 7], [16, 18, 7, None, None, 13, 0]),
    ]
    for i, (input_list, expected) in enumerate(test_cases, 1):
        root = build_tree_from_list(input_list)
        result = tree_to_list(sol.transformTree(root))
        status = "PASS" if result == expected else "FAIL"
        print(f"Test {i}: {status} - Expected: {expected}, Got: {result}")

test_with_level_order()