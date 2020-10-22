

def search_iterative(nums, target):
    if len(nums) == 0:
        return False

    for num in nums:
        if num == target:
            print(num)
            return True

    return False

def search_recursion(nums, target):
    if len(nums) == 0:
        return False

    if nums[0] == target:
        print(nums[0])
        return True

    search_recursion(nums[1:], target)


#  another one
def search_another(nums, target):
    if len(nums) == 0:
        return False

    num = nums.pop()
    if num == target:
        print(num)
        return True

    search_another(nums, target)

search_iterative([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5)
search_recursion([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 8)
search_another([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1)
