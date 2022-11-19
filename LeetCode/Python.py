# 1.Two Sum
class Solution:
    def twoSum(self, nums, target: int):
        for i, val in enumerate(nums):
            for j in range(i, len(nums)):
                if val + nums[j] == target:
                    print('b')
                    return [i, j]


# 2. Add Two Numbers
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    sum_num = 0
    ret, previous_node = None, None

    while l1 is not None or l2 is not None:
        for l in l1, l2:
            if l:
                sum_num += l.val

        if sum_num >= 10:
            node = ListNode(val=sum_num - 10)
            sum_num = 1
        else:
            node = ListNode(val=sum_num)
            sum_num = 0

        if not ret:
            ret = node
            previous_node = node
        else:
            previous_node.next = node
            previous_node = node

        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

    if sum_num:
        previous_node.next = ListNode(val=1)

    return ret

#3 Longest Substring Without Repeating Characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        length = start_i = 0
        end_i = 1
        while end_i < len(s):
            if s[end_i] in s[start_i:end_i]:
                if end_i - start_i > length:
                    length = end_i - start_i
                start_i += s[start_i:end_i].index(s[end_i]) + 1
            end_i += 1

        if length > end_i - start_i:
            return length
        else:
            return end_i - start_i


#4 Median of Two Sorted Arrays'



class Solution:
    #First iteration, signifcantly overthought it
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        def get_val(l1, l2):
            nonlocal i1, i2
            if i1 is not None and i2 is not None:
                if l1[i1] < l2[i2]:
                    val = l1[i1]
                    i1 = i1 + 1 if i1 < len(l1) - 1 else None
                else:
                    val = l2[i2]
                    i2 = i2 + 1 if i2 < len(l2) - 1 else None
            elif i1 is not None:
                val = l1[i1]
                i1 = i1 + 1
            else:
                val = l2[i2]
                i2 = i2 + 1
            return val

        count = median = 0
        if len(nums1) != 0 and len(nums2) != 0:
            i1 = i2 = count = median = 0
            length = (len(nums1) + len(nums2)) / 2
        else:
            if len(nums1) != 0:
                length = len(nums1) / 2
                i1, i2 = 0, None
            else:
                length = len(nums2) / 2
                i1, i2 = None, 0

        while count <= int(length):
            median = get_val(nums1, nums2)

            # Is even
            if count == int(length) - 1:
                if int(length) == length:
                    median = (median + get_val(nums1, nums2)) / 2
                    return median

            count += 1
        return median

    #Second interation, Way simpler and cleaner solution, comparable speed
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        nums = nums1 + nums2
        nums.sort()
        # Even
        if len(nums) % 2 == 0:
            t = nums[len(nums) // 2]
            t2 = nums[len(nums) // 2 - 1]
            return (nums[len(nums) // 2] + nums[len(nums) // 2 + 1]) / 2
        else:
            return nums[len(nums) // 2]

    #3rd iteration, learned that defining a length is faster than calling it multiple times.
    # I was under the misimpression that python functions (i.e. len()) == numpy functions, in that defining a new variable in numpy, even
    # if it is used multiple times later in the function, is slower than using the function itself (e.g. idx = np.argsort(arr), using idx vs using np.argsort(arr)
    # Additionally, learned that !=0 is faster than if(True) and if(foo = 0)
    class Solution:
        def findMedianSortedArrays(self, nums1, nums2) -> float:
            nums = nums1 + nums2
            nums.sort()
            length = len(nums)
            mid = length // 2
            # Even
            if length % 2 != 0:
                return nums[mid]
            else:
                return (nums[mid] + nums[mid - 1]) / 2


t = Solution.findMedianSortedArrays(Solution, [1,2], [3, 4])

