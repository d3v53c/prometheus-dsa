

def insertion_sort(nums):
    """
    Basic Insertion sort implementation.
    """
    for index in range(1, len(nums)):
        currentValue, currentPosition = nums[index], index

        while currentPosition > 0 and currentValue < nums[currentPosition - 1]:
            nums[currentPosition] = nums[currentPosition - 1]
            currentPosition -= 1
        
        nums[currentPosition] = currentValue