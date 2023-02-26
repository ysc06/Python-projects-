"""
File: tree.py
Name: Yu-Shan Cheng
-------------------------
This file shows the basic concepts for binary trees.
After constructing a tree, we will do 4 traversal examples:
Pre-order
In-order 
Post-order
BFS
"""
class TreeNode:
	def __init__(self, left, data, right):
		self.val = data
		self.left = left
		self.right = right

def main():
	# Milestone 1: Construct a tree
	root = None
	leaf1 = TreeNode(None,2,None)
	leaf2 = TreeNode(None,6,None)
	leaf3 = TreeNode(None,18,None)
	leaf4 = TreeNode(None,40,None)
	node1 = TreeNode(leaf1,4,leaf2)
	node2 = TreeNode(leaf3, 19, leaf4)
	root = TreeNode(node1, 17, node2)

	# Milestone 2: 3 ways to traverse a tree
	print('\n---------pre-order--------')
	pre_order(root)
	print('\n---------in-order--------')
	in_order(root)
	print('\n---------post-order--------')
	post_order(root)

	# Milestone 3: Breadth First Search
	print('\n---------bfs--------')
	bfs(root)


def pre_order(root):
	if root is None:
		pass
	else:
	# 中左右
		print(root.val, end=",")
		pre_order(root.left)
		pre_order(root.right)


def in_order(root):
	if root is None:
		pass
	else:
		# 左中右
		in_order(root.left)
		print(root.val, end=",")
		in_order(root.right)

def post_order(root):
	if root is None:
		pass
	else:
		#左右中
		post_order(root.left)
		post_order(root.right)
		print(root.val, end=",")


def bfs(root):
	queue = [root]
	while len(queue) != 0:
		node = queue.pop(0)
		print(node.val, end=" ")
		if node.left is not None:
			queue.append(node.left)
		if node.right is not None:
			queue.append(node.right)
	

if __name__ == '__main__':
	main()
