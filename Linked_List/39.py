# Q39: Reverse a Linked List

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

    def reverse(self):
        prev = None
        curr = self.head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        self.head = prev

    def display(self):
        elements = []
        curr = self.head
        while curr:
            elements.append(str(curr.data))
            curr = curr.next
        print(" -> ".join(elements) if elements else "Empty list")


ll = LinkedList()
values = list(map(int, input("Enter linked list elements (space-separated): ").split()))
for v in values:
    ll.append(v)

print("Original list:  ", end="")
ll.display()

ll.reverse()
print("Reversed list:  ", end="")
ll.display()
