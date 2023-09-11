class TreeNode:

    def __init__(self, elem):
        self.left = None
        self.right = None
        self.elem = elem


def BinaryTreeFromOrderings(inorder, preorder):
    if len(inorder) == 0:
        return None
    node = TreeNode(preorder[0])
    rootIndex = inorder.index(preorder[0])
    node.left = BinaryTreeFromOrderings(inorder[:rootIndex],
                                        preorder[1:rootIndex + 1])
    node.right = BinaryTreeFromOrderings(inorder[rootIndex + 1:],
                                         preorder[rootIndex + 1:])
    print(node.elem, end="")
    return node


if __name__ == "__main__":
    preorder = "GDAFEMHZ"
    inorder = "ADEFGHMZ"
    BinaryTreeFromOrderings(inorder, preorder)
