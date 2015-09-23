from collections import deque


def max_rectangle(lst):
    lst.append(0)
    max_area = 0
    queue = deque()
    queue.append((0, -1))
    for index, bar in enumerate(lst):
        while len(queue) > 1 and queue[-1][0] >= bar:
            height = queue.pop()[0]
            area = height*(index - queue[-1][1] - 1)
            max_area = max(max_area, area)
        queue.append((bar, index))
    return max_area

while True:
    histogram = map(int, raw_input().strip().split(' ')[1:])
    if not histogram:
        break
    print max_rectangle(histogram)
