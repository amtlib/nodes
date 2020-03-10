from tree.node import Node

node = Node()

print('Empty node')
print(node)

print('Set value to 5')
node.set_value(5)
print(node)

print('Create new node with value 3')
node2 = Node()
node2.set_value(3)
print(node2)

print('Set node with value 3 as left node of the old one')
node.set_left_node(node2)

print(node)

print('Parent node values')
print('Sum: ', node.get_sum())
print('Avg: ', node.get_avg())
print('Count: ', node.get_count())
print('Median: ', node.get_median())


print()

print('New node values')
print('Sum: ', node2.get_sum())
print('Avg: ', node2.get_avg())
print('Count: ', node2.get_count())
print('Median: ', node2.get_median())
