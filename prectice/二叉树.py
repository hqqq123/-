class Node:
    def __init__(self,value,left=None,right=None):
        self.data=value
        self.right=right
        self.left=left
# 先序+中序构造二叉树
def ConstructBinTree_preAndTin(pre,tin):

    if pre and tin:
        root=Node(pre[0])
        # print(root.data)
        index=tin.index(root.data)#根节点在中序的位置，也是左子树的长度
        right_length=len(tin)-index-1
        if index>0:
            root.left=ConstructBinTree_preAndTin(pre[1:index+1],tin[:index])
        if right_length>0:
            root.right=ConstructBinTree_preAndTin(pre[index+1:],tin[index+1:])
        return root
# 先序输出，递归
def print_pre(root):
    # print(root.data)
    if root:
        print(root.data, '---')
        print_pre(root.left)
        print_pre(root.right)
# 先序输出，非递归
def print_pre_xh(root):
    stack=[]
    while True:

        if not root:
            root=stack[len(stack)-1]
            del stack[len(stack)-1]
            root=root.right
        if root:
            stack.append(root)
            print(root.data)
            root=root.left
        if not stack:
            break
# 中序输出，递归
def print_tin(root):
    if root:
        print_tin(root.left)
        print(root.data)
        print_tin(root.right)
# 中序输出，非递归
def print_tin_xh(root):
    stack = []
    while True:

        if not root:
            root = stack[len(stack) - 1]
            del stack[len(stack) - 1]
            print(root.data)
            root = root.right
        if root:
            stack.append(root)
            root = root.left
        if not stack:
            break
# 后序输出，递归
def print_later(root):
    if root:
        print_later(root.left)
        print_later(root.right)
        print(root.data)
# 后序输出，非递归
def print_later_xh(root):
    stack = []
    visit = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    while True:
        if root:
            stack.append(root)
            visit[root.data] += 1
            root = root.left
        else:
            root = stack[len(stack) - 1]
            if visit[root.data] == 2:
                del stack[len(stack) - 1]
                print(root.data)
                root = None
            else:
                visit[root.data] += 1
                root = root.right

        if not stack:
            break
# 层序遍历
def layer(root):
    stack=[]
    stack.append(root)
    while stack:
        cur_node=stack[0]
        print(cur_node.data,' ')
        del stack[0]
        if cur_node.left:
            stack.append(cur_node.left)
        if cur_node.right:
            stack.append(cur_node.right)

#求最大树深
def deepLength(root):
    def _length(node):
        if not node:
            return 0
        else:
            return max(_length(node.left),_length(node.right))+1
    return _length(root)
# 判断两棵树是否相同
def is_equal(root1,root2):
    def _equal(root1,root2):
        if not root1 and not root2:
            return True
        elif root1 and root2:
            return root1.data==root2.data and _equal(root1.left,root2.left) and _equal(root1.right,root2.right)

        else:
            return False
    return _equal(root1,root2)
if __name__ == '__main__':
    print('-------')
    pre=[1,2,4,7,3,5,6,8]
    tin=[4,7,2,1,5,3,8,6]
    root=ConstructBinTree_preAndTin(pre,tin)
    # print(root.data)
    # print_pre(root)
    # print_pre_xh(root)

    # print_tin(root)
    # print('----------------')
    # print_tin_xh(root)

    # print_later(root)
    # print_later_xh(root)
    # layer(root)
    pre = [1, 2, 4, 7, 3, 5, 9, 8]
    tin = [4, 7, 2, 1, 5, 3, 8, 9]
    root2 = ConstructBinTree_preAndTin(pre, tin)
    # print(deepLength(root))
    print(is_equal(root,root2))
# li=[1,2,3]
# print(li.index(2))