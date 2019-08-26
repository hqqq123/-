class TreeNode:
    def __init__(self,value):
        self.val=value
        self.right=None
        self.left=None
def ConstructBinaryTree(pre,tin):

    if pre and tin:
        root=TreeNode(pre[0])
        root_tin_index=tin.index(root.val)

        left_length=root_tin_index
        right_length=len(tin)-left_length-1
        if left_length>0:
            root.left=ConstructBinaryTree(pre[1:left_length+1],tin[:left_length])
            print(root.left.val,'l')
        if right_length>0:
            root.right=ConstructBinaryTree(pre[left_length+1:],tin[root_tin_index+1:])
            print(root.right.val,'r')
        return root

if __name__ == '__main__':
    pre=[1,2,4,7,3,5,6,8]
    tin=[4,7,2,1,5,3,8,6]
    root=ConstructBinaryTree(pre,tin)
    print('------------------')
    while root:
        print(root.val)
        print(root.left.val,'lllllllll')
        print(root.right.val,'rrrrrrrrrr')
        root=root.left
