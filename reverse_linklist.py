class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SimpleStack:
    def __init__(self):
        self._container = []

    def push(self, element):
        return self._container.append(element)

    def pop(self):
        return self._container.pop()

    def is_empty(self):
        return not self._container


def reverse_linklist(pHead):
    stack = SimpleStack()
    if not pHead:
        return None
    while pHead:
        stack.push(pHead)
        pHead = pHead.next

    head = stack.pop()
    cur_pos = head
    while not stack.is_empty():
        cur_pos.next = stack.pop()
        cur_pos = cur_pos.next

    cur_pos.next = None

    return head


def print_linklist(head):
    while head:
        print(head.data, end="->")
        head = head.next
    print("None\n")


def main():
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    print_linklist(node1)
    print_linklist(reverse_linklist(node1))


if __name__ == "__main__":
    main()
