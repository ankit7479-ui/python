# stack using List
stack = []
stack.append(2)
stack.append(1)
print(stack.pop())
print(stack.pop())


# stack using Using collections.deque (more efficient)
from collections import deque
stack = deque()
stack.append(3)
stack.append(2)
stack.append(1)
print(stack.pop())
