class ArrayQueue:
    def __init__(self, capacity=13):
        self.data = [None] * capacity
        self.capacity = capacity
        self.head = 0   
        self.tail = 0   

    def size(self):
        return self.tail - self.head

    def is_empty(self):
        return self.head == self.tail

    def enqueue(self, value):
        if self.tail == self.capacity:
            raise OverflowError("Черга переповнена")
        self.data[self.tail] = value   
        self.tail += 1                 
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Черга порожня")
        value = self.data[self.head]
        self.data[self.head] = None
        self.head += 1                 
        return value

    def show(self):
        items = self.data[self.head:self.tail]
        print("Черга (масив):", items if items else "порожня")


# ---------- 2. Черга на основі вузлів ----------
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None   


class LinkedQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def size(self):
        return self._size

    def is_empty(self):
        return self.head is None

    def enqueue(self, value):
        node = Node(value)
        if self.tail is None:         
            self.head = self.tail = node
        else:
            self.tail.next = node    
            self.tail = node           
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Черга порожня")
        value = self.head.data
        self.head = self.head.next     
        if self.head is None:
            self.tail = None
        self._size -= 1
        return value

    def show(self):
        items = []
        cur = self.head
        while cur:
            items.append(cur.data)
            cur = cur.next
        print("Черга (вузли):", items if items else "порожня")



def demo(q, name):
    print(f"\n===== {name} =====")
    q.show()
    print("Порожня?", q.is_empty())
    for x in (6, 4, 6, 2, 7):
        q.enqueue(x)
        print(f"Додано {x}, розмір = {q.size()}")
    q.show()
    print("Видалено:", q.dequeue())
    print("Видалено:", q.dequeue())
    print("Розмір =", q.size())
    q.show()
    q.enqueue(25)
    q.show()
    while not q.is_empty():
        print("Видалено:", q.dequeue())
    q.show()
    try:
        q.dequeue()
    except IndexError as e:
        print("Помилка:", e)


if __name__ == "__main__":
    demo(ArrayQueue(), "ЧЕРГА НА МАСИВІ")
    demo(LinkedQueue(), "ЧЕРГА НА ВУЗЛАХ")