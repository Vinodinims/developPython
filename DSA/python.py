def two_sum(nums: list[int], target: int) -> list[int]:
    """Classic two-sum using hash map. O(n) time, O(n) space."""
    seen = {}  # value -> index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

sum = two_sum([2, 7, 9, 15], 9)  # returns [0, 1]
print(sum)