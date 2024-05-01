
class Queue2:

    empty_msg = "Queue is empty."
    
    def __init__(self):

        self.items = []

    def enqueue(self, item):

        self.items.append(item)
    
    def dequeue(self):

        if self.items == []:
            print(self.empty_msg)
        else:
            return self.items.pop(0)

    def front(self):

        if self.items == []:
            print(self.empty_msg)
        else:
            return self.items[0]
    
    def rear(self):

        if self.items == []:
            print(self.empty_msg)
        else:
            return self.items[-1]