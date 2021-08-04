# -*- utf-8
import os
import shutil


class TreeNode(object):
    def __init__(self, data, left_child=None, right_child=None):
        self.data = data
        self.left_child = left_child
        self.right_child = right_child

    def isNone(self):
        return self.data is None

    def __repr__(self):
        return f"<TreeNode data:{self.data}, left_child:{self.left_child},"\
            + f"right_child: {self.right_child} >"


class Tree(object):
    def __init__(self, root=None):
        self.root = root

    @classmethod
    def create_from_list(self, alist):
        """
        Create tree from list by breadth first
        """
        if not alist:
            return None

        q = Queue()
        data = alist.pop(0)
        root = TreeNode(data)
        q.put(root)

        while alist:
            while not q.isEmpty():
                node = q.get()
                for i in range(2):
                    if alist:
                        child_data = alist.pop(0)
                        # if child_data:
                        child_node = TreeNode(child_data)
                        if i % 2 == 0:
                            node.left_child = child_node
                        else:
                            node.right_child = child_node
                        q.put(child_node)

        return root

    @classmethod
    def pre_order_traverse(self, node):
        if not node:
            return None
        print(node.data, end=" ")
        self.pre_order_traverse(node.left_child)
        self.pre_order_traverse(node.right_child)

    @classmethod
    def in_order_traverse(self, node):
        if not node:
            return None
        self.in_order_traverse(node.left_child)
        print(node.data, end=" ")
        self.in_order_traverse(node.right_child)

    @classmethod
    def post_order_traverse(self, node):
        if not node:
            return None
        self.post_order_traverse(node.left_child)
        self.post_order_traverse(node.right_child)
        print(node.data, end=" ")

    @classmethod
    def breadth_first_traverse(self, node):
        if not node:
            return None
        q = Queue()
        q.put(node)
        while not q.isEmpty():
            node = q.get()
            print(node.data, end=" ")
            if node.left_child:
                q.put(node.left_child)
            if node.right_child:
                q.put(node.right_child)

        print("")

    @classmethod
    def max_depth(self, node):
        if not node:
            return 0
        return 1 + max(self.max_depth(node.left_child),
                       self.max_depth(node.right_child))

    @classmethod
    def is_full_binary_tree(self, node):
        if not node or node.isNone():
            return False
        if node.left_child and node.right_child:
            return self.is_full_binary_tree(
                node.left_child) and self.is_full_binary_tree(node.right_child)
        else:
            return not node.left_child and not node.right_child

    @classmethod
    def is_complete_binary_tree(self, node):
        return all(Tree.toList(node))

    @staticmethod
    def toList(node):
        result = []
        if not node:
            return result
        q = Queue()
        q.put(node)
        while not q.isEmpty():
            node = q.get()
            result.append(node.data)
            if node and node.left_child:
                q.put(node.left_child)
            if node and node.right_child:
                q.put(node.right_child)

        return result


class Queue(object):
    def __init__(self):
        self._container = []

    def put(self, data):
        self._container.append(data)

    def get(self):
        return self._container.pop(0)

    def isEmpty(self):
        return not self._container

    def get_size(self):
        return len(self._container)


def test_tree(alist):
    print("======================================")
    temp_alist = alist[:]
    tree = Tree.create_from_list(temp_alist)
    print(f"Max depth: {Tree.max_depth(tree)}")
    print(f"Is full: {Tree.is_full_binary_tree(tree)}")
    print(f"Is complete: {Tree.is_complete_binary_tree(tree)}")
    print(f"originList: {alist}")
    print(f"treetoList: {Tree.toList(tree)}")
    print("\npre_order_traverse:")
    Tree.pre_order_traverse(tree)
    print("\nin_order_traverse:")
    Tree.in_order_traverse(tree)
    print("\npost_order_traverse:")
    Tree.post_order_traverse(tree)
    print("\nbreadth_first_traverse:")
    Tree.breadth_first_traverse(tree)


if __name__ == "__main__":
    print(os.sys)
    print(shutil)
    alist0 = [1, 2, 3, 4, 5, 6, 7, 8]
    alist1 = [1, 2, 3, 4, 5, 6, 7]
    alist2 = [1, 2, 3, 4, 5, None, 6]
    alist3 = [10, 9, 8, 4, 5, None, 6, 50, 60, 70, None, 80, 90, 55, 65]

    test_tree(alist0)
    test_tree(alist1)
    test_tree(alist2)
    test_tree(alist3)
