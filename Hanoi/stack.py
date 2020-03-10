'''
    Data structure that model LIFO
    Last In First Out
'''
class Stack:
    def __init__(self):
        self._container = []

    def push(self, item):
        self._container.append(item)

    def pop(self):
        return self._container.pop()

    def __repr__(self):
        return repr(self._container)
