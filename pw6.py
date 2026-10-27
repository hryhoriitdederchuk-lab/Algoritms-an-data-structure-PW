class Node:
    """Вузол стека: data - дані, next - посилання на попередній вузол."""

    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node


class Stack:
    """Стек, реалізований за допомогою вузлів (посилань)."""

    def __init__(self):
        self.top = None      
        self._size = 0

    def is_empty(self):
        return self.top is None

    def push(self, item):
        """Вставляє елемент на вершину стека."""
        self.top = Node(item, self.top)
        self._size += 1

    def peek(self):
        """Повертає елемент з вершини, не видаляючи його."""
        if self.is_empty():
            raise IndexError("Стек порожній")
        return self.top.data

    def pop(self):
        """Повертає елемент з вершини та видаляє його."""
        if self.is_empty():
            raise IndexError("Стек порожній")
        data = self.top.data
        self.top = self.top.next
        self._size -= 1
        return data

    def clear(self):
        """Видаляє всі елементи зі стека."""
        self.top = None
        self._size = 0

    def count(self):
        """Повертає кількість елементів (підрахунок обходом вузлів)."""
        n = 0
        current = self.top
        while current is not None:
            n += 1
            current = current.next
        return n

    def size(self):
        """Повертає кількість елементів (збережений лічильник)."""
        return self._size

    def toString(self):
        """Усі елементи від вершини до дна, без видалення."""
        items = []
        current = self.top
        while current is not None:
            items.append(str(current.data))
            current = current.next
        return "Стек (вершина -> дно): [" + ", ".join(items) + "]"

    def __str__(self):
        return self.toString()


if __name__ == "__main__":
    s = Stack()
    print("Порожній?", s.is_empty())

    for value in (11, 22, 33):
        s.push(value)
        print(f"push({value})")

    print(s)
    print("peek():", s.peek())
    print("count():", s.count())
    print("size():", s.size())

    print("pop():", s.pop())
    print(s)
    print("size() після pop:", s.size())

    s.clear()
    print("Після clear():", s)
    print("Порожній?", s.is_empty())

    try:
        s.pop()
    except IndexError as e:
        print("Помилка при pop() з порожнього стека:", e)