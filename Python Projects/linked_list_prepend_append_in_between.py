"""
File: linked_list_prepend_append_in_between.py
Name: 
--------------------------
This file shows 3 main operations on 
manipulating a linked list:
- Prepend
- Append
- In between
"""


class ListNode:
	def __init__(self, data, pointer):
		self.val = data
		self.next = pointer


def main():
	linked_list = None
	##### Construct linked_list #####
	linked_list = ListNode(("A",3), None)
    linked_list.next = ListNode(("B", 5), None)
	linked_list.next.next = ListNode(("C", 7), None)
	print("Original linked_list: ")
	traversal(linked_list)
	#################################

	######## Prepend ########
	new_node = ListNode(("Z", 0), None)
	new_node.next= linked_list
	linked_list=new_node
		print("After prepending ('Z', 0): ")
	traversal(linked_list)
	#########################

	######## Append #########
	new_node = ListNode(("D",9), None)
	cur = linked_list
	while cur.next is not None:
		cur = cur.next
	cur.next = new_node
	print("After appending ('D', 9): ")
	traversal(linked_list)
	#########################

	######### In between ############
	new_node = ListNode (("X", 5), None)
	cur = linked_list
	while cur is not None and cur.next is not None:
		if cur.val[1] <= new_node.val[1] < cur.next.val[1]:
			new_node.next = cur.next
			cur.next = new_node
			break
		else:
			cur=cur.next
	print("After inserting ('X', 5): ")
	traversal(linked_list)
	#################################
	

def traversal(linked_list):
	"""
	:param linked_list: ListNode, holding the first ListNode object 
						as the start of priority queue
	--------------------------
	This function prints out each val of a linked list
	"""
	cur = linked_list
	while cur is not None:
		print(cur.val)
		cur = cur.next


if __name__ == '__main__':
	main()
