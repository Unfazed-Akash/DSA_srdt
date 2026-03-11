# Q41: Find the Middle Node of a Linked List
# Uses the slow/fast pointer (tortoise and hare) technique

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

    def find_middle(self):
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data if slow else None

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

print("Linked list: ", end="")
ll.display()
print(f"Middle node value: {ll.find_middle()}")
