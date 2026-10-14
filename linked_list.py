class Node:
    """
    A Node class to store integer data and a reference to the next node.
    """

    def __init__(self, data):
        # The value this node holds (e.g., an employee ID).
        self.data = data
        # Reference to the following node; None means this is the last node.
        self.next = None


class LinkedList:
    """
    A singly linked list that holds Node objects and performs operations using recursion.

    Recursion fits linked lists naturally: a list is either empty (None) or a
    node followed by a smaller list. Each recursive helper below handles one
    node and delegates "the rest of the list" to a recursive call.
    """

    def __init__(self):
        # An empty list has no first node.
        self.head = None

    def insert_at_front(self, data):
        """Insert a new node at the start of the list in O(1) time."""
        new_node = Node(data)
        # The new node points at the old head, then becomes the head.
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        """Append a new node to the end of the list in O(n) time."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        # Walk to the last node (the one whose 'next' is None).
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def recursive_sum(self):
        """Return the sum of all node data, computed recursively."""

        def _sum(node):
            # Base case: past the end of the list, nothing left to add.
            if node is None:
                return 0
            # Recursive case: this node's value plus the sum of the rest.
            return node.data + _sum(node.next)

        return _sum(self.head)

    def recursive_reverse(self):
        """Reverse the list in-place, recursively, and update 'head'."""

        def _reverse(prev, current):
            # Base case: we've run off the end; 'prev' is the old tail,
            # which is the new head.
            if current is None:
                return prev
            # Save the rest of the list before re-pointing this node.
            next_node = current.next
            # Flip this node's pointer to face backward.
            current.next = prev
            # Recursive case: advance one step, with 'current' as the new 'prev'.
            return _reverse(current, next_node)

        self.head = _reverse(None, self.head)

    def recursive_search(self, target):
        """Return True if 'target' is in the list, otherwise False."""

        def _search(node):
            # Base case 1: reached the end without finding the target.
            if node is None:
                return False
            # Base case 2: found it, so stop recursing.
            if node.data == target:
                return True
            # Recursive case: keep looking in the rest of the list.
            return _search(node.next)

        return _search(self.head)

    def display(self):
        """Print the list as 'val -> val -> val -> None' and return that string."""
        values = []
        current = self.head
        while current is not None:
            values.append(str(current.data))
            current = current.next
        output = " -> ".join(values + ["None"])
        print(output)
        return output
