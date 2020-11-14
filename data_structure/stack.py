# -*- coding:utf-8 -*-

class Empty(Exception):
    pass


class ListStack:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def push(self, e):
        self._data.append(e)

    def top(self):
        if self.is_empty():
            raise Empty('stack is empty.')
        return self._data[-1]

    def pop(self):
        if self.is_empty():
            raise Empty('stack is empty.')
        return self._data.pop()


S = ListStack()
S.push(5)
S.push(8)
print(len(S))
print(S.top())
print(S.pop())
print(S.is_empty())
print(S.top())
print(S.pop())
print(S.is_empty())
print(S.pop())


