"""
You are given a binary tree. You need to write a function that can determine if
it is a valid binary search tree.

The rules for a valid binary search tree are:

- The node's left subtree only contains nodes with values less than the node's
value.
- The node's right subtree only contains nodes with values greater than the
node's value. (implys no duplicates because doesn't say equal to)
- Both the left and right subtrees must also be valid binary search trees.

Example 1:
Input:

    5
   / \
  3   7

Output: True

Example 2:
Input:

    10
   / \
  2   8
     / \
    6  12

Output: False
Explanation: The root node's value is 10 but its right child's value is 8.

Example 3:
    10
   /   \
   2   18
       / \
      6  21
This would return False
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

#def is_valid_BST(self, root):
    # Your code here
    #keep track of the valid range as we are traversing down the tree
    #when we go left, limit the upper bound to be root -1
    # when we go right, limit the lower bound to be root +1
    #check if the current nodes value falls within the range
    #check the roots left child
    # if left child >= root, return False
    #check the roots right child
    # if right child <= root, return False
    #else return True
    #return recurse(root, float('-inf'), float('inf')) #this will start our recursive function

def recurse(root, min_bound, max_bound): #traverses the entire tree in WORST case, O(n)
    # base case #1
    # we've gone through whole tree, never saw False, so return True
    if root is None:
        return True
    # base case #2
    #if the current value falls out of the range, return False
    if root.value < min_bound or root.value > max_bound:
        return False
    #how do we get closer to our base case?
    #recurse with the left child and update the range according to the rules
    left = recurse(root.left, min_bound, root.value - 1)
    # recurse with the right child and update the range according to the rules
    right = recurse(root.right, root.value + 1, max_bound)
    #if either left or right is False, return False
    return left and right #if one of these is False, it will return False,
    ## if these are both True, will return True

#Alternative strategy, use in order ordering
# if the BST is valid, then an in- order traversal will produce a sorted array
def is_sorted(elements): #elements is a list
    #traverse elements two at a time
    for i in range(1, len(elements)):
        if elements[i] < elements[i - 1]:
            return False
    return True

def in_order_traverse(root, result):
    if root is None:
        return
    in_order_traverse(root.left, result)
    result.append(root.value)
    in_order_traverse(root.right, result)

def is_valid_BST(root): # O(n + n)  ~ O(2 * n) ~ 0(n)
    elements = []
    in_order_traverse(root, elements)
    print(elements)
    return is_sorted(elements)




bst = TreeNode(10)
bst.left = TreeNode(2)
bst.right = TreeNode(18)
bst.right.left = TreeNode(6)
bst.right.right = TreeNode(21)

bst2 = TreeNode(5)
bst2.right = TreeNode(7)
bst2.left = TreeNode(2)
print(is_valid_BST(bst))
print(is_valid_BST(bst2))
