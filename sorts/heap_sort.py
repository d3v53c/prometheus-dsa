

def heapify(nums, size, root_index):
    """
    Implementation for a Max Heap from array.
    """
    # Assume the index of the largest element is the root index
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2

    # If the left child of the root is a valid index, and the element is greater
    # than the current largest element, then update the largest element
    if left_child < size and nums[left_child] > nums[root_index]:
        largest = left_child

    # Do the same for the right child of the root
    if right_child < size and nums[right_child] > nums[root_index]:
        largest = right_child

    # If the largest element is no longer the root element, swap them
    if largest != root_index:
        nums[largest], nums[root_index] = nums[root_index], nums[largest]
        # Heapify the new root element to ensure it's the largest
        heapify(nums, size, largest)


def heap_sort(nums):
    """
    Basic Heap sort implementation.
    """
    n = len(nums)

    for i in range(n, -1, -1):
        heapify(nums, n, i)

    for i in range(n - 1, 0, -1):
        nums[0], nums[i] = nums[i], nums[0]
        heapify(nums, i, 0)
