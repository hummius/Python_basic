class Stack:
    """
    Класс Стэк

    Attributes:
        __stack_list: список для элементов стэка
    """
    def __init__(self):
        self.__stack_list = []

    def __str__(self):
        return '; '.join(self.__stack_list)

    def check_stack(self, elem):
        """
        Функция для проверки наличия запрашиваемого элемента в стэке

        :param elem: запрашиваемый элемент

        :return: True если он есть
        """
        if elem in self.__stack_list:
            return True

    def delete_elem(self, elem):
        """
        Функция удаления запрашиваемого элемента из стэка

        :param elem: запрашиваемый элемент
        :return:
        """
        self.__stack_list.remove(elem)

    def push(self, elem):
        """
        Функция добавления в список стэка элемента

        :param elem: элемент для добавления
        :return:
        """
        self.__stack_list.append(elem)

    def pop(self):
        if len(self.__stack_list) == 0:
            return None
        return self.__stack_list.pop()

class TaskManager:
    """
    Класс Менеджер Задач
    """
    def __init__(self):
        self.task = dict()

    def __str__(self):
        """
        Функция для вывода на экран информации о задачах и их приоритетов

        :return: ''.join(display)
        """
        display = []
        if self.task:
            for i_priority in sorted(self.task.keys()):
                display.append(f'{i_priority} {self.task[i_priority]}\n')
        return ''.join(display)
    def new_task(self, task, priority):
        """
        Функция для создания новой задачи с приоритетом

        :param task: задача
        :param priority: уровень приоритета
        :return:
        """
        if priority not in self.task:
            self.task[priority] = Stack()
        self.task[priority].push(task)

    def task_delete(self, task):
        """
        Функция для удаления задачи из менеджера задач.
        Удаляется задача с большим приоритетом.

        :param task: задача для удаления

        :return:
        """
        for elem in self.task:
            if self.task[elem].check_stack(task):
                self.task[elem].delete_elem(task)
                break


manager = TaskManager()
manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 1)
manager.new_task("поесть", 2)
manager.new_task("сдать дз", 2)
print(manager)
manager.task_delete("поесть")
print(manager)
manager.task_delete("поесть")
print(manager)