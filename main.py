class Stack:
    class Node:
        def __init__(self, data, prev=None):
            self.data = data
            self.prev = prev

    def __init__(self):
        self.__count = 0
        self.__top = None

    def is_empty(self) -> None:
        """
        Функция проверяет стек на пустоту для функций pop и peek
        при пустом стеке безопасно завершает запрос возвращая None
        :return:
        """
        if self.__count == 0: return

    def push(self, elem) -> None:
        """
        Функция помещает очередной elem на вершину стека
        :param elem: добавляемый элемент
        :return: None
        """
        node = Stack.Node(elem)

        if not self.is_empty():
            node.prev = self.__top

        self.__top =node
        self.__count += 1

    def peek(self) -> None: #(хотел написать Self)
        """
        Функция получает значение поля data объекта с вершины стека
        :return: поле data объекта Node
        """
        if not self.is_empty():
            return self.__top.data

    def pop(self) -> None: #(хотел написать Self)
        """
        Функция удаляет объект с вершины стека возвращая его поле data
        :return:
        """
        if not self.is_empty():
            target = self.__top.data
            self.__top= self.__top.prev
            self.__count -= 1
            return target

    def __get_count(self):
        return self.__count

    count = property(__get_count)
