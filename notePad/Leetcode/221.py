# Definition for a binary tree node.
from typing import List, Optional


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.val)
    inorder(root.right)

def postorder(root):
    if root is None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.val)

def preorder(root):
    if root is None:
        return
    print(root.val)
    preorder(root.left)
    preorder(root.right)

tr27 = TreeNode(27); tr55 = TreeNode(55)

# first
tree = TreeNode(67)
# second & third
tree.left = TreeNode(30, TreeNode(34), tr27)
tree.right = TreeNode(70, TreeNode(66), tr55)
# forth
tr27.left = TreeNode(12)
tr55.left = TreeNode(41)

# inorder(tree)
# print("——————————————————————————————————————————")
# preorder(tree)

inorder = [9, 3, 15, 20, 7]
postorder = [9, 15, 7, 20, 3]
"""
1.抓住右序遍历根节点永远在最右边的规律
2.通过右序遍历得到的根节点，在中序遍历中递归寻找整颗数
——————————————————————————————————————————————————
3.通过对右序遍历列表的操作, 保留递归层数位置的数据
退出条件：没有多的数字给找到的根节点做子树
"""
"""
草稿：
先打印退出条件的数为：

参考一: https://leetcode.cn/problems/construct-binary-tree-from-inorder-and-postorder-traversal/solutions/426738/cong-zhong-xu-yu-hou-xu-bian-li-xu-lie-gou-zao-14/?envType=daily-question&envId=2024-02-21
"""
def printTree(root, level=0, prefix="Root:"):
    if root is not None:
        print(" " * (level * 4) + prefix, root.val)
        printTree(root.left, level + 1, "L:")
        printTree(root.right, level + 1, "R:")

class Solution:
    def buildTree(self, inorder, postorder) -> TreeNode:
        def helper(in_left, in_right, flag="right"):
            # 如果这里没有节点构造二叉树了，就结束
            if in_left > in_right:
                return None

            # 选择 post_idx 位置的元素作为当前子树根节点
            val = postorder.pop()
            root = TreeNode(val)

            # 根据 root 所在位置分成左右两棵子树
            index = idx_map[val]
            print(index)
            print(root.val, in_left, in_right, flag)

            # 构造右子树
            root.right = helper(index + 1, in_right, "right")
            # 构造左子树
            root.left = helper(in_left, index - 1, "left")
            return root

        # 建立（元素，下标）键值对的哈希表
        idx_map = {val: idx for idx, val in enumerate(inorder)}
        return helper(0, len(inorder) - 1)


inorder = [-4,-10,3,-1,7,11,-8,2]
postorder = [-4,-1,3,-10,11,-8,2,7]
# inorder = [9, 3, 15, 20, 7]
# postorder = [9, 15, 7, 20, 3]
# printTree(Solution().buildTree(inorder, postorder))

print("——————————————————————————————————————————————————")

class Solution(object):
    def buildTree(self, inorder, postorder):
        def hRecursion(before, after, postorder, depth, flag="right") -> TreeNode:
            if (len(before) == 0 and len(after) == 0) or len(postorder) == 0:
                return
            root = postorder[-1]  # 选择 post_idx 位置的元素作为当前子树根节点
            out = TreeNode(root)

            rootIndex = inorder.index(root)
            print(root, inorder, rootIndex, postorder) # 后续遍历的最后一个值在中序遍历中的索引带入后续遍历中就是下一个根节点的值

            after = inorder[rootIndex + 1:]
            before = inorder[0:rootIndex]

            if root in inorder: inorder.remove(root)

            out.left = hRecursion(before, [], postorder[:rootIndex], depth, "left")
            out.right = hRecursion([], after, postorder[rootIndex: -1], depth + 1, "right")

            # postorder.pop()  # 在处理完左右子树后再 pop, 放在这里平均执行更快

            return out
        return hRecursion([], inorder, postorder, 0)

# inorder = [1, 2]
# postorder = [2, 1]
# inorder = [9, 3, 15, 20, 7]
# postorder = [9, 15, 7, 20, 3]
# inorder = [-1]
# postorder = [-1]
# inorder = [1,2,3,4]
# postorder = [1,4,3,2]
inorder = [-4,-10,3,-1,7,11,-8,2]
postorder = [-4,-1,3,-10,11,-8,2,7]
printTree(Solution().buildTree(inorder, postorder))

print("——————————————————————————————————————————————————")
"""
之前上面的方法无法在递归的时候正确回到相应的层数，因为递归的时候层数没有保留，所以在递归的时候无法正确回到相应的层数
通过参考该方法,利用对右序递归的操作保留层数数据
抓住不论中序还是后序左节点永远先遍历的特点
参考二: https://leetcode.cn/problems/construct-binary-tree-from-inorder-and-postorder-traversal/solutions/2647794/tu-jie-cong-on2-dao-onpythonjavacgojsrus-w8ny/
"""
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int], depth) -> Optional[TreeNode]:
        if not postorder:  # 空节点
            return None
        left_size = inorder.index(postorder[-1])  # 左子树的大小
        print(depth)
        left = self.buildTree(inorder[:left_size], postorder[:left_size], depth + 1)
        right = self.buildTree(inorder[left_size + 1:], postorder[left_size: -1], depth + 1)
        return TreeNode(postorder[-1], left, right)

inorder = [-4,-10,3,-1,7,11,-8,2]
postorder = [-4,-1,3,-10,11,-8,2,7]
# printTree(Solution().buildTree(inorder, postorder, 0))



# class Solution(object):
#     def buildTree(self, inorder, postorder):
#         def hRecursion(before, after, depth, flag="right") -> TreeNode:
#             if (len(before) == 0 and len(after) == 0) or len(postorder) == 0:
#                 return
#             root = postorder.pop()
#             out = TreeNode(root)
#
#             rootIndex = inorder.index(root)
#
#             after = inorder[rootIndex + 1:]
#             before = inorder[0:rootIndex]
#             print(depth, root, before, after)
#             # temppost = postorder
#             # tempin = inorder.copy()
#
#             if root in inorder: inorder.remove(root)
#             # if len(before) == 1:
#             #     num = before.pop()
#             #     out.left = TreeNode(num)
#             #     if num in inorder: inorder.remove(num)
#             #     if num in postorder: postorder.remove(num)
#             #     print(num)
#             # # else:
#             # #     out.left = TreeNode(None)
#             # if len(after) == 1:
#             #     num = after.pop()
#             #     out.right = TreeNode(num)
#             #     if num in inorder: inorder.remove(num)
#             #     if num in postorder: postorder.remove(num)
#             #     print(num)
#             # if len(before) != 1 or len(after) != 1:
#             #     if len(postorder) > 0:
#             # print(depth, tempin.index(postorder[len(postorder) - 1]), rootIndex, flag)
#             out.left = hRecursion(before, [], depth, "left")
#             # if tempin.index(postorder[len(postorder) - 1]) >= rootIndex:
#             out.right = hRecursion([], after, depth + 1, "right")
#             # else:
#
#             return out
#         return hRecursion([], inorder, 0)
