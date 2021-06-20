# -*- utf-8


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return f"<Node data:{self.data} next:{self.next}>"


class LinkedList:
    def __init__(self):
        self.head = None
        self._size = 0
        self.reset_pos()

    def append(self, data):
        node = Node(data)
        print(node)

        if self.head:
            tail = self.get_tail()
            tail.next = node
        else:
            self.head = node
            self.reset_pos()

        self._size += 1

    def new_head(self, data):
        node = Node(data)

        node.next = self.head
        self._current_pos = self.head = node
        self._size += 1

    def reset_pos(self):
        self._current_pos = self.head

    def find_node(self, data):
        node = None
        while True:
            try:
                if self._current_pos.data == data:
                    node = self._current_pos
                    break
                self._current_pos = self._current_pos.next
            except AttributeError:
                break
        self.reset_pos()
        return node

    def find_prev(self, node):
        prev_node = None
        while True:
            try:
                if self._current_pos.next is node:
                    prev_node = self._current_pos
                    break
                self._current_pos = self._current_pos.next
            except AttributeError:
                break
        self.reset_pos()
        return prev_node

    def left_insert(self, data, new_data):
        node = self.find_node(data)
        if not node:
            raise ValueError(f'Can not find data:{data} in the linkedList.')

        elif node is self.head:
            self.new_head(data)
        else:
            prev_node = self.find_prev(node)
            new_node = Node(new_data)
            prev_node.next = new_node
            new_node.next = node
            self._size += 1

    def right_insert(self, data, new_data):
        found = []
        while self._current_pos.next:
            if self._current_pos.data == data:
                found.append(self._current_pos)
            self._current_pos = self._current_pos.next
        self.reset_pos()
        if not found:
            raise ValueError(f'Can not find data:{data} in the linkedList.')

        new_node = Node(new_data)
        new_node.next = found[-1].next
        found[-1].next = new_node
        self._size += 1

    def indexOf(self, data):
        i = -1
        while True:
            i += 1
            try:
                if self._current_pos.data == data:
                    self.reset_pos()
                    return i
                self._current_pos = self._current_pos.next
            except AttributeError:
                break
        self.reset_pos()
        return -1

    def remove(self, data):
        node = self.find_node(data)
        prev_node = self.find_prev(node)
        prev_node.next = node.next
        self._size -= 1
        self.reset_pos()
        return node.data

    def get_size(self):
        return self._size

    def get_head(self):
        return self.head

    def get_tail(self):
        while self._current_pos.next:
            self._current_pos = self._current_pos.next

        tail = self._current_pos
        self.reset_pos()
        return tail

    def toList(self):
        return [node for node in self]

    def __iter__(self):
        return self

    def __next__(self):
        if self._current_pos:
            data = self._current_pos.data
            self._current_pos = self._current_pos.next
            return data
        else:
            self.reset_pos()
            raise StopIteration()

    def __repr__(self):
        return f"<LinkedList size:{self.get_size()}>"

    def toGraph(self):
        s = ""
        for data in self:
            s += f"{data} => "
        s += "None"
        return s


if __name__ == "__main__":
    ll = LinkedList()
    for i in range(5):
        ll.append(i)

    from IPython import embed
    embed()
