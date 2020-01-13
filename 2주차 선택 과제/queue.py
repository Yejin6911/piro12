class queue:
    def __init__(self):
        self.__arr = []
        self.__rear = 0
        self.__front = 0

    def push(self, item):
        self.__arr.append(item)
        self.__rear += 1

    def isEmpty(self):
        if self.__arr==[]:
            return True
        else:
            return False
        
    def pop(self):
        if self.isEmpty():
            return False
        else:
            item = self.__arr[self.__front]
            del (self.__arr[self.__front])
            return item

    def peek(self):
        if self.isEmpty():
            return False
        else:
            return(self.__arr[self.__front])
