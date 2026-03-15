from collections import deque
nums = [1, 3, -1, -3, 5, 3, 6, 7]

k = 3

dq = deque()
res = []

for right in range(len(nums)):
    while dq and nums[dq[-1]] < nums[right]:
        dq.pop()
    dq.append(right)
    if dq[0] < right - k + 1:
        dq.popleft()
    if right >= k - 1:
        res.append(nums[dq[0]])
print(res)