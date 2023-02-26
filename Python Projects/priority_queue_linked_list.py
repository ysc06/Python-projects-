"""
File: priority_queue_linked_list.py
Name: Yu-Shan Cheng
--------------------------
This file shows how to construct a linked list 
from scratch and use it to implement a priority queue.
"""


# It breaks the user inputs
EXIT = ''


class ListNode:
	def __init__(self, data, pointer):
		self.val = data
		self.next = pointer


def main():
	priority_queue = None
	print('--------------------------------')
	# TODO:
	while True:
		name = input("Patient: ")
		if name == EXIT:
			break
		priority = int(input("Priority: "))
		data = (name, priority)
		new_node = ListNode(data, None)

		if priority_queue is None:
			# First Data
			priority_queue = new_node
		else:
			# Prepend
			if priority_queue.val[1] > priority:
				new_node.next = priority_queue
				priority_queue = new_node
			else:
				# Append
				cur = priority_queue
				while cur.next is not None:
					cur = cur.next
				# cur at the end
				if cur.val[1] <= priority:
					cur.next = new_node
				else:
					# In between
					cur = priority_queue
					while cur is not None and cur.next is not None:
						if cur.val[1] <= new_node.val[1] < cur.next.val[1]:
							new_node.next = cur.next
							cur.next = new_node
							break
						else:
							cur = cur.next
	print('--------------------------------')
	traversal(priority_queue)


def traversal(priority_queue):
	"""
	:param priority_queue: ListNode, holding the first ListNode object 
						   as the start of priority queue
	--------------------------
	This function prints out each val of a linked list
	"""
	cur = priority_queue
	while cur is not None:
		print(cur.val)
		cur = cur.next


if __name__ == '__main__':
	main()
