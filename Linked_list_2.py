class ObjList:

    def __init__(self, data):
        self.__data = data
        self.__next = None
        self.__prev = None

    def set_next(self, obj):
        self.__next = obj

    def get_next(self):
        return self.__next

    def set_prev(self, obj):
        self.__prev = obj

    def get_prev(self):
        return self.__prev

    def set_data(self, data):
        self.__data = data

    def get_data(self):
        return self.__data

class LinkedList:
    data_list = []
    def __init__(self):
        self.head = None
        self.tail = None

    def add_obj(self, obj):
        if isinstance(obj, ObjList):
            if self.head == None:
                self.head = obj
                self.data_list.append(obj.get_data())
                self.tail = obj
            elif self.head == self.tail:
                self.tail = obj
                self.head.set_next(obj)
                self.tail.set_prev(self.head)
                self.data_list.append(obj.get_data())
            else:
                self.tail.set_next(obj)
                obj.set_prev(self.tail)
                self.tail = obj
                self.data_list.append(obj.get_data())

    def get_data(self):
        return self.data_list

    def remove_obj(self):
        if self.head != self.tail:
            self.data_list.pop()
            self.tail = self.tail.get_prev()
            self.tail.set_next(None)
        else:
            self.head = None
            self.tail = None

lst = LinkedList()
lst.add_obj(ObjList("данные 1"))
lst.add_obj(ObjList("данные 2"))
lst.add_obj(ObjList("данные 3"))
res = lst.get_data()

print(res)
lst.remove_obj()
print(res)
