from typing import Optional, Any


class Node:
    """
    Класс Узел

    Attributes:
        value: значение
        next: ссылка на следующий узел
    """
    def __init__(self, value: Optional[Any] = None, next: Optional['Node'] = None) -> None:
        self.value = value
        self.next = next

    def __str__(self) -> str:
        return f'Node {self.value}'


class LinkedList:
    """
    Класс Односвязный список

    Attributes:
        head: указатель на головной узел
        length: длина списка
    """
    def __init__(self) -> None:
        self.head: Optional[Node] = None
        self.length = 0

    def __str__(self) -> str:
        if self.head is not None:
            current = self.head
            values = [str(current.value)]
            while current.next is not None:
                current = current.next
                values.append(str(current.value))
            return f'{values}'
        return 'LinkedList []'

    def append(self, elem: Any) -> None:
        """
        Функция-метод дополнения элемента в конец списка

        :param elem: элемент для дополнения списка
        :return: None
        """
        new_node = Node(elem)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        self.length += 1

    def get(self, index) -> Optional[Node]:
        """
        Функция-метод для получения элемента списка по индексу

        :param index: индекс элемента

        :return: элемент списка
        """
        cur_node = self.head
        cur_index = 0
        if self.length == 0 or self.length < index:
            raise IndexError
        if cur_node is not None:
            if index == 0:
                return self.head.value
        while cur_node is not None:
            if cur_index == index:
                return cur_node.value
            cur_node = cur_node.next
            cur_index += 1

    def remove(self, index) -> None:
        """
        Функция-метод для удаления элемента списка по индексу

        :param index: индекс элемента для удаления

        :return: None
        """
        cur_node = self.head
        cur_index = 0
        if self.length == 0 or self.length <= index:
            raise IndexError
        if cur_node is not None:
            if index == 0:
                self.head = cur_node.next
                self.length -= 1
                return
        while cur_node is not None:
            if cur_index == index:
                break
            prev = cur_node
            cur_node = cur_node.next
            cur_index += 1

        prev.next = cur_node.next
        self.length -= 1


my_list = LinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)
print('Текущий список:', my_list)
print('Получение третьего элемента:', my_list.get(2))
print('Удаление второго элемента.')
my_list.remove(1)
print('Новый список:', my_list)
