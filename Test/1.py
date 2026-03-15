
nums = [-4, -1, 0, 3, 10]
left = 0
right = len(nums) - 1

result = [0] *len(nums)

p = len(nums) - 1

while left <= right:
    left_square = nums[left] * nums[left]
    right_square = nums[right] * nums[right]

    if left_square > right_square:
        result[p] = left_square
        left += 1
    else:
        result[p] = right_square
        right -= 1
    p -= 1
print(result)