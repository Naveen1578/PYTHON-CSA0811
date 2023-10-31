def searchRange(nums, target):
    def binary_search(left, right, is_lower_bound):
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target or (is_lower_bound and nums[mid] == target):
                left = mid + 1
            else:
                right = mid
        return left

    left_index = binary_search(0, len(nums), True)
    right_index = binary_search(0, len(nums), False) - 1

    if left_index <= right_index and right_index < len(nums) and nums[right_index] == target:
        return [left_index, right_index]
    else:
        return [-1, -1]

# Example usage:
nums = [5,7,7,8,8,10]
target = 8
print(searchRange(nums, target)) # Output: [3,4]
