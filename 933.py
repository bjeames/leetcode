from collections import deque

# q = deque()
# q.append(10)      # enqueue
# x = q.popleft()   # dequeue

class RecentCounter:

    def __init__(self):
        self.queue = deque()

    def ping(self, t: int) -> int:
        self.queue.append(t)
        local_queue = self.queue
        min_time = t - 3000
        while local_queue[0] < min_time:
            local_queue.popleft()
        return len(local_queue)

        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)

# remember that popping left makes iteration different than a normal list, i.e. queue[0] changes
# every time you popleft()