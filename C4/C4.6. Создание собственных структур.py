class Node:  # класс элемента
    def __init__(self, value=None, next_=None):  # инициализируем
        self.value = value  # значением
        self.next = next_  # и ссылкой на следующий элемент

    def __str__(self):
        return "Node value = " + str(self.value)


class LinkedList:  # класс списка
    def __init__(self):  # инициализируем пустым
        self.first = None
        self.last = None

    def clear(self):  # очищаем список
        self.__init__()

    def __str__(self):  # функция печати
        R = ''

        pointer = self.first  # берём первый указатель
        while pointer is not None:  # пока указатель не станет None
            R += str(pointer.value)  # добавляем значение в строку
            pointer = pointer.next  # идём дальше по указателю
            if pointer is not None:  # если он существует, добавляем пробел
                R += ' '
        return R

    def pushleft(self, value):
        if self.first is None:
            self.first = Node(value)
            self.last = self.first
        else:
            new_node = Node(value, self.first)
            self.first = new_node

    # Напишите функцию pushright, которая добавляет элемент в правую часть списка.
    def pushright(self, value):
        if self.first is None:
            self.first = Node(value)
            self.last = self.first
        else:
            new_node = Node(value)
            self.last.next = new_node
            self.last = new_node

    """ 
 С удалением элементов несколько интереснее. Удалить элемент из начала можно без особого труда: достаточно изменить 
 указатель на первый элемент. Удалить элемент из конца более затруднительно, потому что, удалив последний элемент, мы
  потеряем ссылку на него. В таком случае время выполнения операции будет равно
  Существуют способы улучшить и этот аспект. Одно из решений — создание двусвязного списка, в котором помимо указателя 
  на следующий элемент будет храниться указатель и на предыдущий элемент. Или можно модифицировать односвязный список, 
  сохраняя ещё и указатель на предпоследний элемент. Оба способа требуют дополнительной памяти, но в данном случае мы 
  пожертвуем производительностью ради памяти и скорости разработки (что тоже важно, кстати).
 """

    def popleft(self):
        if self.first is None:  # если список пустой, возвращаем None
            return None
        elif self.first == self.last:  # если список содержит только один элемент
            node = self.first  # сохраняем его
            self.__init__()  # очищаем
            return node  # и возвращаем сохранённый элемент
        else:
            node = self.first  # сохраняем первый элемент
            self.first = self.first.next  # меняем указатель на первый элемент
            return node  # возвращаем сохранённый

        "И немного более сложная процедура удаления последнего элемента:"

    def popright(self):
        if self.first is None:  # если список пустой, возвращаем None
            return None
        elif self.first == self.last:  # если список содержит только один элемент
            node = self.first  # сохраняем его
            self.__init__()  # очищаем
            return node  # и возвращаем сохраненный элемент
        else:
            node = self.last  # сохраняем последний
            pointer = self.first  # создаём указатель
            while pointer.next is not node:  # пока не найдём предпоследний
                pointer = pointer.next
            pointer.next = None  # обнуляем указатели, чтобы
            self.last = pointer  # предпоследний стал последним
            return node  # возвращаем сохранённый
# LL = LinkedList()
# LL.pushright(1)
# LL.pushleft(2)
# LL.pushright(3)
# LL.popright()
# LL.pushleft(4)
# LL.pushright(5)
# LL.popleft()
# print(LL)

# Теперь, наконец, напишем функционал этого класса, чтобы он стал полноценным итератором.

    def __iter__(self):  # объявляем класс как итератор
        self.current = self.first  # в текущий элемент помещаем первый
        return self  # возвращаем итератор

    def __next__(self):  # метод перехода
        if self.current is None:  # если текущий стал последним
            raise StopIteration  # вызываем исключение
        else:
            node = self.current  # сохраняем текущий элемент
            self.current = self.current.next  # совершаем переход
            return node  # и возвращаем сохранённый

#И в заключение напишем «магический» метод, возвращающий размер структуры данных.

    def __len__(self):
        count = 0
        pointer = self.first
        while pointer is not None:
            count += 1
            pointer = pointer.next
        return count

LL = LinkedList()
LL.pushright(1)
LL.pushleft(2)
LL.pushright(3)
LL.popright()
LL.pushleft(4)
LL.pushright(5)
LL.popleft()
print(LL.__len__())