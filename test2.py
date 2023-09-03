class Stack:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def push(self, data):
        self.items.append(data)
    def pop(self):
        return self.items.pop()

    def display(self):
        print('Stack elements: ')
        print(self.items)
s = Stack()
while True:
    print('Type spelling as per option displayed')
    print('push <value>')
    print('pop')
    print('disp')
    print('quit')
    do = input('What would you like to do? ').split()
    operation = do[0].strip().lower()
    if operation == 'push':
        s.push(int(do[1]))
    elif operation == 'pop':
        if s.is_empty():
               print('pop Stack is empty.')
        else:
            print('Popped value: ', s.pop())
    elif operation == 'disp':
        if s.is_empty():
            print('diaplay Stack is empty.')
        else:
            s.display()
    elif operation == 'quit':
        break