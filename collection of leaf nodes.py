class TreeNode:
    def __init__(self, data):
        self.data = data 
        self.left = None 
        self.right = None 
 
def collectLeafNodes(root, result):
    if root == None:
        return 
    if root.left == None and root.right == None:
        result.append(root.data)
        return
 
    collectLeafNodes(root.left, result)
    collectLeafNodes(root.right, result)
 
def printLeafNodes(root):
    result = []
    collectLeafNodes(root, result)
    print("Leaf Nodes:", result)
 
# objects creation (memory allocation) 
root = TreeNode(18)
obj2 = TreeNode(15)
obj3 = TreeNode(20)
obj4 = TreeNode(25)
obj5 = TreeNode(30)
obj6 = TreeNode(45)
obj7 = TreeNode(80)
 
# establishing links between nodes 
root.left = obj2 
root.right = obj3 
 
obj2.left = obj4 
obj2.right = obj5 
 
obj3.left = obj6 
obj3.right = obj7

printLeafNodes(root)
