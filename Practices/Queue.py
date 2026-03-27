from collections import deque


queue = deque()
queue.append(1)
queue.append(2)
queue.append(3)
print(queue.popleft())
print(queue[0])

# Priority Queue
import heapq

pq = []
heapq.heappush(pq, (4, "task1"))
heapq.heappush(pq, (2, "task2"))
heapq.heappush(pq, (6, "task3"))

while pq:
    priority,task = heapq.heappop(pq)
    print(f"{task} (priority{priority})")
