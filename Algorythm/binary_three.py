from binarytree import tree, bst, Node, build


class MyNode:

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


a = tree(height=4, is_perfect=False)
print(a)

b = bst(height=3, is_perfect=True)
print(b)

c = Node(7)
c.left = Node(3)
c.right = Node(11)
c.left.left = Node(11)

print(c)

d = build([7, 3, 11, 1, 5, 9, 3, None, 2, None])
print(d)
