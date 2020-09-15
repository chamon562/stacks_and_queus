class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    

class Stack:
    def __init__(self):
        self.stack = []
    
    def __str__(self):
        return str(self.stack)

    def push(self, new_node):
        # self.head = Node(data, self.head)
        self.stack.append(new_node.data)
    
    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        return None
    def size(self):
        # checking size is similar to checking length
        return len(self.stack)
    def __len__(self):
        return self.size()

    def is_empty(self):
        return len(self.stack ) == 0

# for a list its append, for a stack its push

new_node = Node("Stack")
another_node = Node("stack2")
stacks_on_stacks = Stack()
# push in some data
stacks_on_stacks.push(new_node)
stacks_on_stacks.push(another_node)

print(stacks_on_stacks)
stacks_on_stacks.pop()
print(stacks_on_stacks)

stacks_on_stacks.push(Node("Stack3"))

print(stacks_on_stacks.size())
print(stacks_on_stacks.is_empty())