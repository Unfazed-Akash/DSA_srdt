# Q40: Detect Loop in a Linked List (Floyd's Cycle Detection Algorithm)

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

    def create_loop(self, pos):
        """Create a loop by connecting last node to the node at given position (0-indexed)."""
        nodes = []
        curr = self.head
        while curr:
            nodes.append(curr)
            curr = curr.next
        if nodes and 0 <= pos < len(nodes):
            nodes[-1].next = nodes[pos]

    def has_loop(self):
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


ll = LinkedList()
values = list(map(int, input("Enter linked list elements (space-separated): ").split()))
for v in values:
    ll.append(v)

create = input("Create a loop for testing? (yes/no): ").strip().lower()
if create == "yes":
    pos = int(input(f"Enter loop position (0 to {len(values) - 1}): "))
    ll.create_loop(pos)

if ll.has_loop():
    print("Loop DETECTED in the linked list")
else:
    print("No loop detected in the linked list")
