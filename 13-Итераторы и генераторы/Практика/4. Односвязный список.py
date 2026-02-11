class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __str__(self):
    #     if self.head is None:
    #         return "[]"
    #
    #     elements = []
    #     current = self.head
    #
    #     while current is not None:
    #         elements.append(str(current.data))
    #         current = current.next
    #     return f"[{" ".join(elements)}]"
        str_r = ' '.join(str(i) for i in self)
        return f"[{str_r}]"

    def __init__(self):
        self.head = None
        self.lenght = 0

    def __iter__(self):
        current = self.head

        while current is not None:
            yield current.data
            current = current.next

    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.lenght += 1
            return

        last = self.head
        while last.next is not None:
            last = last.next
        last.next = new_node
        self.lenght += 1

    def get_index(self, index):
        if index < 0 or index >= self.lenght:
            raise IndexError("Индекс вне диапазона")

        current_node = self.head
        for i in range(index):
            current_node = current_node.next
        return current_node.data

    def remove(self, index):
        if index < 0 or index >= self.lenght:
            raise IndexError("Индекс вне диапазона")

        if index == 0:
            self.head = self.head.next
            self.lenght -= 1
            return

        prev = None
        current = self.head
        current_index = 0

        while current_index < index:
            prev = current
            current = current.next
            current_index += 1

        prev.next = current.next
        self.lenght -= 1


    def print_list(self):
        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

lst = LinkedList()
lst.append(10)
lst.append(20)
lst.append(30)
lst.print_list()
lst.remove(0)

# lst.print_list()
# print(lst.get_index(0))
# print(lst.get_index(1))
# # print(lst.get_index(2))
# # print(lst.get_index(3))

# for i in lst:
#     print(i)
#
# for i in lst:
#     print(i)

print(lst)