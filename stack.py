class Stack():
    def __init__(self, collection: list = []) -> None:
        self.collection = collection

    def push(self, value):
        self.collection.append(value)

    def pop(self):
        return self.collection.pop()

    def peek(self):
        return self.collection[-1] if self.size() > 0 else False

    def size(self):
        return len(self.collection)

    def isEmpty(self):
        return self.size() == 0
