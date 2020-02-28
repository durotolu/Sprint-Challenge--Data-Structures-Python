from doubly_linked_list import DoublyLinkedList
from doubly_linked_list import ListNode


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()
        self.wildcard = None

    def append(self, item):
        if self.storage.length == self.capacity:
            if self.wildcard == self.storage.tail:
                self.storage.remove_from_head()
                self.storage.add_to_head(item)
                self.wildcard = self.storage.head
            else:
                value = ListNode(item)
                value.prev = self.wildcard.next.prev
                value.next = self.wildcard.next.next
                if self.wildcard.prev:
                    self.wildcard.prev = value
                if self.wildcard.next:
                    self.wildcard.next = value
                    if self.wildcard.next.next:
                        self.wildcard.next.next.prev = value
                if value and value.next is None:
                    self.storage.tail = value
                    self.wildcard = self.wildcard.next
                else:
                    self.wildcard = self.wildcard.next


            # self.wildcard = self.storage.tail
            # if self.wildcard.next is None:
            #     wildcard = self.storage.head
            # else:
            #     wildcard = self.wildcard.next
            # wildcard.prev.next = item
            # wildcard.next.prev = item
            return
        self.storage.add_to_tail(item)
        self.wildcard = self.storage.tail

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        current = self.storage.head
        while current is not None:
            list_buffer_contents.append(current.value)
            current = current.next
        # for item in self.storage:
        #     list_buffer_contents.append()

        return list_buffer_contents

buffer = RingBuffer(5)
buffer.append('a')
buffer.append('b')
buffer.append('c')
buffer.append('d')
buffer.append('e')
buffer.append('f')
buffer.append('g')
buffer.append('h')
buffer.append('i')
buffer.append('j')
buffer.append('k')

print(buffer)

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
