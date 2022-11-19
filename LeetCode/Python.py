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
