# Q42: Merge Two Sorted Linked Lists

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def display(self):
        elements = []
        curr = self.head
        while curr:
            elements.append(str(curr.data))
            curr = curr.next
        print(" -> ".join(elements) if elements else "Empty list")


def merge_sorted_lists(l1_head, l2_head):
    dummy = Node(0)
    curr = dummy
    a, b = l1_head, l2_head
    while a and b:
        if a.data <= b.data:
            curr.next = a
            a = a.next
        else:
            curr.next = b
            b = b.next
        curr = curr.next
    curr.next = a if a else b
    return dummy.next


ll1 = LinkedList()
ll2 = LinkedList()

vals1 = list(map(int, input("Enter first sorted linked list (space-separated): ").split()))
vals2 = list(map(int, input("Enter second sorted linked list (space-separated): ").split()))

for v in vals1:
    ll1.append(v)
for v in vals2:
    ll2.append(v)

print("List 1: ", end="")
ll1.display()
print("List 2: ", end="")
ll2.display()

merged_head = merge_sorted_lists(ll1.head, ll2.head)
result_ll = LinkedList()
result_ll.head = merged_head

print("Merged: ", end="")
result_ll.display()
