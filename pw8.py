class Node:
    """Вузол бінарного дерева: значення + посилання на лівого та правого нащадка."""

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    """Бінарне дерево пошуку. Зберігає посилання на кореневий вузол."""

    def __init__(self):
        self.root = None
        self._count = 0


    def add(self, value):
        new_node = Node(value)
        self._count += 1

        # дерево порожнє – новий вузол стає коренем
        if self.root is None:
            self.root = new_node
            return

        current = self.root
        while True:
            if value < current.value:   
                if current.left is None:
                    current.left = new_node
                    return
                current = current.left
            else:                          
                if current.right is None:
                    current.right = new_node
                    return
                current = current.right


    def contains(self, value):
        current = self.root
        while current is not None:
            if value == current.value:
                return True
            current = current.left if value < current.value else current.right
        return False


    def remove(self, value):
        """Повертає True, якщо елемент було видалено, інакше False."""
        parent = None
        current = self.root

        # 1. шукаємо вузол та його батька
        while current is not None and current.value != value:
            parent = current
            current = current.left if value < current.value else current.right

        if current is None:
            return False  # елемента немає


        if current.left is not None and current.right is not None:
            heir_parent = current
            heir = current.right
            while heir.left is not None:
                heir_parent = heir
                heir = heir.left

            current.value = heir.value  


            if heir_parent is current:
                heir_parent.right = heir.right
            else:
                heir_parent.left = heir.right
        else:

            child = current.left if current.left is not None else current.right
            if parent is None:
                self.root = child
            elif parent.left is current:
                parent.left = child
            else:
                parent.right = child

        self._count -= 1
        return True


    def get_all(self):
        result = []
        self._in_order(self.root, result)
        return result

    def _in_order(self, node, result):
        if node is not None:
            self._in_order(node.left, result)
            result.append(node.value)
            self._in_order(node.right, result)

    def print_all(self):
        print("Елементи дерева:", self.get_all())


    def max(self):
        if self.root is None:
            return None
        current = self.root
        while current.right is not None:
            current = current.right
        return current.value


    def min(self):
        if self.root is None:
            return None
        current = self.root
        while current.left is not None:
            current = current.left
        return current.value


    def count(self):
        return self._count


if __name__ == "__main__":
    tree = BinaryTree()

    print("=== Додавання елементів ===")
    for v in [3, 1, 2, 9, 7, 10, 6, 8]:
        tree.add(v)
        print(f"Додано: {v}")
    tree.print_all()

    print("\n=== Пошук елемента ===")
    for v in [7, 5]:
        print(f"Елемент {v} є в дереві: {tree.contains(v)}")

    print("\n=== Найбільший / найменший / кількість ===")
    print("Найбільший елемент:", tree.max())
    print("Найменший елемент:", tree.min())
    print("Кількість елементів:", tree.count())

    print("\n=== Видалення елементів ===")
    print("Видалення вузла з одним нащадком (1):", tree.remove(1))
    tree.print_all()
    print("Видалення листка (6):", tree.remove(6))
    tree.print_all()
    print("Видалення вузла з двома нащадками (9):", tree.remove(9))
    tree.print_all()
    print("Видалення кореня з двома нащадками (3):", tree.remove(3))
    tree.print_all()
    print("Видалення неіснуючого елемента (100):", tree.remove(100))

    print("\n=== Стан після видалення ===")
    print("Найбільший елемент:", tree.max())
    print("Найменший елемент:", tree.min())
    print("Кількість елементів:", tree.count())
    print("Корінь дерева:", tree.root.value)