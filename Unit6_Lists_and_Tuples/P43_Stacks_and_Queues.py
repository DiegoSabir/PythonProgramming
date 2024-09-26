stack1 = []
stack1.append(1)
stack1.append(2)
stack1.append(3)

print(stack1)

element = stack1.pop()

queue1 = []
queue1.append(1)
queue1.append(2)
queue1.append(3)

print(queue1)

element = queue1.pop(0)

from collections import deque
queue1 = deque()

queue1.append(1)
queue1.append(2)
queue1.append(3)

print(queue1)

element = queue1.popleft()