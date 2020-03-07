from models.tree import Tree


# Create new tree
tree = Tree()

tree.add_value(5)
tree.add_value(4)
tree.add_value(6)
tree.add_value(1)
tree.add_value(7)
tree.add_value(5.5)

print(tree)
print(tree.length())
print(tree.get_sum())
print(tree.get_levels())
print(tree.avg())
print(tree.inorder_traversal())
print(tree.median())