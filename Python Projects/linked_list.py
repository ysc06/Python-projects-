"""
File: linked_list.py
Name: Yu-Shan Cheng
--------------------------
This file shows how to construct a linked list 
from scratch and use it to implement a priority queue.
"""

class ListNode:  # class就像在包記憶體. Constructor在定義記憶體會長什麼樣子
	def __init__(self, data, pointer):
		self.val = data  # value 包 data
		self.next = pointer # next 包 pointer

def main():
	# 倒著串
	# node3 = ListNode(("C", 7), None)
	# node2 = ListNode(("B", 5), node3)
	# node1 = ListNode(("A", 3), node2)
	# linked_List = node1

	#正著串
	node1 = ListNode(("A", 3), None)
	node2 = ListNode(("B", 5), None)
	node3 = ListNode(("C", 7), None)
	node1.next = node2
	node2.next = node3
	linked_list = node1
	traversal(linked_list)


def traversal(linked_list):  # 把所有資料印出來
	cur = linked_list  # 讓cur 來做，不用linked_list。否則memory leak
	while cur.next is not None:   # while cur is not None == OBOB
		print(cur.val)
		cur = cur.next   # infinite loop
	print(cur.val)






if __name__ == '__main__':
	main()
