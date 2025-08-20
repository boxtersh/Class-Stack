class Stack:
    class Node:
        def __init__(self, data, prev=None):
            self.data = data
            self.prev = prev

    def __init__(self):
        self.__size = 0
        self.__top = None

    def __check_is_empty(self) -> None:
        """
        Функция проверяет стек на пустоту для функций pop и peek
        при пустом стеке безопасно завершает запрос возвращая None
        :return:
        """
        if self.__size == 0: return

    def push(self, elem) -> None:
        """
        Функция помещает очередной elem на вершину стека
        :param elem: добавляемый элемент
        :return: None
        """
        node = Stack.Node(elem)

        if self.__top is None:
            self.__top = node

        else:
            node.prev, self.__top = self.__top, node

        self.__size += 1

    def peek(self) -> None: #(хотел написать Self)
        """
        Функция получает значение поля data объекта с вершины стека
        :return: поле data объекта Node
        """
        self.__check_is_empty()

        return self.__top.data

    def pop(self) -> None: #(хотел написать Self)
        """
        Функция удаляет объект с вершины стека возвращая его поле data
        :return:
        """
        self.__check_is_empty()
        target = self.__top.data
        self.__top, self.__size = self.__top.prev, self.__size - 1

        return target

    def __get_size(self):
        return self.__size

    def __get_data(self):
        return self.__top.data

    size = property(__get_size)
    data = property(__get_data)