from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self._data = []
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._data == []

    def enqueue(self, value):
        self._data.append(value)
        self._size += 1

    def dequeue(self):
        if not self.is_empty():
            self._size -= 1
            return self._data.pop(0)
        else:
            return None

    def search(self, index):
        if 0 <= index < self._size:
            return self._data[index]
        else:
            raise IndexError("Índice Inválido ou Inexistente")
