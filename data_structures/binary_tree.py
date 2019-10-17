
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def set_value(self, new_value):
        self.value = new_value

    def set_right(self, node):
        self.right = node

    def set_left(self, node):
        self.left = node

    def get_value(self):
        return self.value

    def get_right(self):
        return self.right

    def get_left(self):
        return self.left

    def balanced(self):
        return self.left and self.right

class BinaryTree:

    def __init__(self, root_node=None):
        self.root_node = root_node

    def set_root(self, new_root):
        self.root_node = new_root

    def _post_order(self, node):
        if node:
            return 1 + self._post_order(node.get_left()) + self._post_order(node.get_right())
        return 0
            # self._post_order(node.get_left())
            # self._post_order(node.get_right())
            # print(node.get_value())

# pos = 10
# commands = []
# while pos > 0:
# 	if pos % 2 == 0:
# 		commands.append('R')  # turn Right
# 	else:
# 		commands.appned('L')  # turn Left
# 	pos = int(pos - 1/2)

    def length(self):
        return self._post_order(self.root_node)

    def add_node(self, item):
        new_node = TreeNode(item)
        if self.root_node == None:
            self.root_node = new_node
        else:
            position = self._post_order(self.root_node)

            backtrack = []
            right = 0
            left = 1
            start = self.root_node

            while position > 0:
                if position % 2 == 0:
                    backtrack.insert(0, right)
                else:
                    backtrack.insert(0, left)
                position = int((position - 1) / 2)

            final = backtrack.pop()
            for command in backtrack:
                if command:
                    #Turn left
                    start = start.get_right()
                else:
                    #Turn right
                    start = start.get_right()
            if final:
                start.set_left(new_node)
            else:
                start.set_right(new_node)



            #self._add_node_recursive(self.root_node, new_node)

    # def _check_tree_balance(self, node):
    #     if node == None:
    #         return False
    #     if not node.left and not node.right
    #         return True
    #     elif _check_tree_balance(node.get_left() and _check_tree_balance(node.get_right))

    # def _add_node_recursive(self, current, to_add)
    #     if current.balanced():
    #         if current.get_left().balanced and current.get_right().balanced()
    #             if 
    #             return _add_node_recursive(current.get_right, to_add)
    #         elif current.get_left.balanced() and not current.get_right.balanced():
    #             return _add_node_recursive(current.get_right(), to_add)
    #         else:
    #             return _add_node_recursive(current.get_left(), to_add)
    #     else:
    #         if current.left == None and current.right == None:
    #             current.set_left(to_add)
    #         elif current.left and not current.right:
    #             current.set_right(to_add)
    #         else:
    #             return _add_node_recursive(current.get_left(), to_add)


new_tree = BinaryTree()
new_tree.add_node("Finally")
new_tree.add_node("Another")
new_tree.add_node("Answer")
print(new_tree.length())
    
