
class Solution:
    # 1.Two Sum
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

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
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

    # 3 Longest Substring Without Repeating Characters
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

    # 4 Median of Two Sorted Arrays'
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
            return (nums[len(nums) // 2] + nums[len(nums) // 2 + 1]) / 2
        else:
            return nums[len(nums) // 2]

    # Third iteration, learned that defining a length is faster than calling it multiple times.
    # I was under the misimpression that python functions (i.e. len()) == numpy functions, in that defining a new variable in numpy, even
    # if it is used multiple times later in the function, is slower than using the function itself (e.g. idx = np.argsort(arr), using idx vs using np.argsort(arr)
    # Additionally, learned that !=0 is faster than if(True) and if(foo == val)

    def findMedianSortedArrays(self, nums1, nums2) -> float:
        nums = nums1 + nums2
        nums.sort()
        length = len(nums)
        mid = length // 2
        if length % 2 != 0:
            return nums[mid]
        else:
            return (nums[mid] + nums[mid - 1])

    # 5. Longest Palindromic Substring
    # This problem was exceptionally challenging for me, but I ended up getting a solution that beats 86% run time and 58 % memory
    # It isn't properly optimized - it has parity checks twice (as helper is called twice)
    # It also doesn't account for the fact that a found palindrome does not need to be rechecked if the indexes are
    # a subsection of an already checked palindrome (as the iteration does not change if a long palindrome is found)
    # will attempt to fix in future solution, but need to take a break from this problem : )
    def longestPalindrome(self, s: str) -> str:
        def helper(i_start, i_end):
            nonlocal s, length, i_start_end

            if s[i_start] != s[i_end]:
                return

            while i_start - 1 >= 0 and i_end + 1 < length:
                if s[i_start - 1] != s[i_end + 1]:
                    break
                i_start -= 1
                i_end += 1

            if i_end - i_start > i_start_end[1] - i_start_end[0]:
                i_start_end = (i_start, i_end)

        length = len(s)
        if length == 1:
            return s

        i_start_end = (0, 1) if s[0] == s[1] else (0, 0)
        for i in range(1, len(s) - 1):
            helper(i, i + 1)
            helper(i - 1, i + 1)

        return s[i_start_end[0]:i_start_end[1] + 1]

    #6. Zigzag Conversion is is is
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        step = numRows + (numRows - 2)
        length = len(s)
        mid = ''
        for row_i in range(1, min(numRows - 1, length)):
            start_step = step - int((row_i * step) / (numRows - 1))
            while row_i < length:
                mid += s[row_i]
                if row_i + start_step >= length:
                    break
                mid += s[row_i + start_step]
                row_i += step

        return s[0::step] + mid + s[numRows - 1::step]

    #7. Reverse Integer

    #First iteration
    def reverse(self, x: int) -> int:
        num_is_negative = x < 0
        num = str(x)[1:][::-1] if num_is_negative else str(x)[::-1]
        length = len(num)

        if length < 10:
            return -int(num) if num_is_negative else int(num)
        elif length > 10:
            return 0

        comp_val = 2 ** 31 if num_is_negative else 2 ** 31 -1
        comp_divider= 10 ** 9

        for i in range(0, 10):
            digit = int(num[i])
            comp = comp_val // comp_divider
            if digit > comp:
                return 0
            elif digit < comp:
                break
            comp_val -= (comp_divider * comp)
            comp_divider /= 10

        return -int(num) if num_is_negative else int(num)

print(Solution.reverse(Solution, 1563847412))
t = 10 ** 9
for _ in range(0, 9):
    t /= 10
print('b')