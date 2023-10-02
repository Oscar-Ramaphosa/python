
''' Creating class for the binary tree'''
class Node(object):
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

'''the binary tree class that has a root on it, this will be used in printing the 
tress also.'''
class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    '''This is the function that prints a tree'''
    def print_tree(self,type):
        if type == "preorder":
            return self.preorderFunction(tree.root, "")
        elif type == "inorder":
            return self.inorderFunction(tree.root, "")
        else:
            return False

    '''The preoder function that checks the tree traversal'''
    def preorderFunction(self, sta, trav):
        '''checks from root to left and Right'''
        if sta:
            trav += (str(sta.value) + " ")
            trav = self.preorderFunction(sta.left, trav)
            trav = self.preorderFunction(sta.right, trav)
        return trav

    '''The inoder function that checks the tree traversal'''
    def inorderFunction(self, sta, trav):
        '''checks from Left to Root and to Right'''
        if sta:
            trav = self.inorderFunction(sta.left, trav)
            trav += (str(sta.value) + " ")
            trav = self.inorderFunction(sta.right, trav)
        return trav

'''this is the tree set up'''
tree = BinaryTree("E")
tree.root.left = Node("X")
tree.root.right = Node("F")
tree.root.left.left = Node("A")
tree.root.left.right = Node("M")
tree.root.right.left = Node("U")
tree.root.right.right = Node("N")

'''printing the Tree'''
print ("The inorder traversal yiels :")
print(tree.print_tree("inorder"))
print("The preorder traversal yiels :")
print(tree.print_tree("preorder"))





