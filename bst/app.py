from tree.tree import Tree


# Create new tree
tree = Tree()

tree.add_value(5)
tree.add_value(4)
tree.add_value(6)
tree.add_value(1)
tree.add_value(7)
tree.add_value(10)

print("Tree:")

print(tree)
print("Count: ", tree.get_count())
print("Sum: ", tree.get_sum())
print("Levels: ", tree.get_levels())
print("Avg: ", tree.get_avg())
print("Inorder traversal: ", tree.get_inorder_traversal())
print("Median: ", tree.get_median())
print("Find node with value 6", tree.find(6))