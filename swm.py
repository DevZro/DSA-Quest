# Sliding Window Maximum

def maxSlidingWindow(nums, k):
    # Implement Max Heap
    heap = [None] * len(nums)

    for i in range(k):
        heap[i] = nums[i]
        walk = i
        while walk != 0 and heap[walk] > heap[walk//2]:
            heap[walk], heap[walk//2] = heap[walk // 2], heap[walk]
            walk = walk // 2

    removed = {}
    cvhp = k # Current Valid Heap Position
    max_values = [0] * (len(nums) - k + 1)

    max_values[0] = heap[0]

    for i in range(k, len(nums)):
        new = nums[i]
            
        # Store in removed so we can check against
        # in case it ever seems like current maximum has not already been removed
        removed[nums[i - k]] = 1 + removed.get(nums[i - k], 0)

        # Add new to heap
        heap[cvhp] = new
        walk = cvhp
        while walk != 0 and heap[walk] > heap[walk//2]:
            heap[walk], heap[walk//2] = heap[walk // 2], heap[walk]
            walk = walk // 2
        cvhp += 1
        # Add to maximum values, if that value hasn't already been removed
        while removed.get(heap[0], 0) != 0: # remove
            removed[heap[0]] -= 1
            heap[0], heap[cvhp - 1] = heap[cvhp - 1], None

            walk = 0
            
            while (2 * walk + 1 < len(heap)) and (heap[2 * walk + 1] != None):
                if ((heap[2 * walk + 2] != None) and (heap[walk] < heap[2 * walk + 1] or heap[walk] < heap[2 * walk + 2])) or (heap[walk] < heap[2 * walk + 1]):
                    if (heap[2 * walk + 2] == None) or heap[2 * walk + 1] > heap[2 * walk + 2]:
                        heap[walk], heap[2 * walk + 1] = heap[2 * walk + 1], heap[walk]
                        walk =  2 * walk + 1
                    else:
                        heap[walk], heap[2 * walk + 2] = heap[2 * walk + 2], heap[walk]
                        walk =  2 * walk + 2
                else:
                    break
            cvhp -= 1
        max_values[i - k + 1] = heap[0]
        
    return max_values