class Queue:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def enqueue(self, value):
        self._data.append(value)

    def dequeue(self):
        firstRemoved = self._data.pop(0)
        return firstRemoved

    def search(self, index):
        if (index > self.__len__() - 1 or index < 0):
            raise IndexError()
        return self._data[index]
