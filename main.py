from random import randint


class Node:
    def __init__(self, key_value, color, parent, left=None, right=None):
        self.key_value = key_value
        self.color = color  # 0 for red, 1 for black
        self.parent = parent
        self.left = left
        self.right = right

    def __repr__(self):
        return f"Key = {self.key_value}, Color = {self.get_color()}"

    def get_color(self):
        COLORS = {0: "RED", 1: "BLACK"}
        return COLORS[self.color]


class RedBlackTree:
    def __init__(self):
        self.NIL_LEAF = Node(None, 1, None)
        self.root = self.NIL_LEAF

    def __repr__(self):
        if self.root != self.NIL_LEAF:
            return "\n".join(self.to_list())
        return "Empty tree"

    def insert(self, key_value):
        new_node = Node(key_value, 0, None, self.NIL_LEAF, self.NIL_LEAF)
        if self.root == self.NIL_LEAF:
            self.root = new_node
            self.root.color = 1
        else:
            current = self.root
            while current != self.NIL_LEAF:
                new_node.parent = current
                if new_node.key_value <= current.key_value:
                    current = current.left
                else:
                    current = current.right

            if new_node.parent.key_value <= new_node.key_value:
                new_node.parent.right = new_node
            else:
                new_node.parent.left = new_node

            self.fix_insert(new_node)

    def rotate_left(self, node):
        right_child = node.right
        node.right = right_child.left

        if right_child.left != self.NIL_LEAF:
            right_child.left.parent = node

        right_child.parent = node.parent

        if node.parent is None:
            self.root = right_child
        elif node == node.parent.left:
            node.parent.left = right_child
        else:
            node.parent.right = right_child

        right_child.left = node
        node.parent = right_child

    def rotate_right(self, node):
        left_child = node.left
        node.left = left_child.right

        if left_child.right != self.NIL_LEAF:
            left_child.right.parent = node

        left_child.parent = node.parent

        if node.parent is None:
            self.root = left_child
        elif node == node.parent.right:
            node.parent.right = left_child
        else:
            node.parent.left = left_child

        left_child.right = node
        node.parent = left_child

    def fix_insert(self, node):
        while node.color == 0 and node.parent.color == 0:
            if node.parent == node.parent.parent.right:
                uncle = node.parent.parent.left
                if uncle.color == 0:
                    node.parent.color = 1
                    uncle.color = 1
                    node.parent.parent.color = 0
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.rotate_right(node)

                    node.parent.color = 1
                    node.parent.parent.color = 0
                    self.rotate_left(node.parent.parent)
            else:
                uncle = node.parent.parent.right

                if uncle.color == 0:
                    node.parent.color = 1
                    uncle.color = 1
                    node.parent.parent.color = 0
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.rotate_left(node)

                    node.parent.color = 1
                    node.parent.parent.color = 0
                    self.rotate_right(node.parent.parent)
            if node == self.root:
                break

        self.root.color = 1

    def swap_color(self, node):
        node.color = 1 - node.color
        if node.left != self.NIL_LEAF:
            node.left.color = 1 - node.left.color
        if node.right != self.NIL_LEAF:
            node.right.color = 1 - node.right.color

    def inorder_traversal(self, node, result, level):
        if node != self.NIL_LEAF:
            self.inorder_traversal(node.right, result, f"\t{level}")
            result.append(f"{level}{node}")
            self.inorder_traversal(node.left, result, f"\t{level}")

    def to_list(self):
        result = []
        level = ""
        self.inorder_traversal(self.root, result, level)
        return result


if __name__ == '__main__':
    # Example usage:
    rb_tree = RedBlackTree()
    i = 0
    keys = []
    while i < 12:
        key = randint(0, 100)
        if key not in keys:
            keys.append(key)
            i += 1
    for key in keys:
        rb_tree.insert(key)
        print(f"---\n{rb_tree}\n---")

    print("Red-Black Tree in-order traversal:")
    print(rb_tree)