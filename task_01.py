'''
Структури даних. Сортування. Робота з однозв'язним списком
1.написати функцію, яка реалізує реверсування однозв'язного списку, змінюючи посилання між вузлами;
2.розробити алгоритм сортування для однозв'язного списку, наприклад, сортування вставками або злиттям;
3.написати функцію, що об'єднує два відсортовані однозв'язні списки в один відсортований список.
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
    
    # Task 1: Reverse the linked list
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
    
    # Task 2: Sort the linked list using merge sort
    def sort(self):
        self.head = self._merge_sort(self.head)
    
    def _merge_sort(self, head):
        if not head or not head.next:
            return head
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second_half = slow.next
        slow.next = None
        left = self._merge_sort(head)
        right = self._merge_sort(second_half)
        return self._merge(left, right)
    
    # Static function for merging
    @staticmethod
    def _merge(left, right):
        dummy = Node(0)
        current = dummy
        while left and right:
            if left.data <= right.data:
                current.next = left
                left = left.next
            else:
                current.next = right
                right = right.next
            current = current.next
        current.next = left if left else right
        return dummy.next
    
    # Task 3: Merge two sorted linked lists
    @staticmethod
    def merge_sorted_lists(list1, list2):
        result = LinkedList()
        result.head = LinkedList._merge(list1.head, list2.head)
        return result

# Test the functions
def test_linked_list():
    print("Test 1: Reversing a linked list")
    list1 = LinkedList()
    for data in [1, 2, 3, 4]:
        list1.append(data)
    print("Original list:", end=" ")
    list1.print_list()
    list1.reverse()
    print("Reversed list:", end=" ")
    list1.print_list()
    print()
    
    print("Test 2: Sorting a linked list")
    list2 = LinkedList()
    for data in [4, 2, 1, 3]:
        list2.append(data)
    print("Unsorted list:", end=" ")
    list2.print_list()
    list2.sort()
    print("Sorted list:", end=" ")
    list2.print_list()
    print()
    
    print("Test 3: Merging two sorted linked lists")
    list3 = LinkedList()
    for data in [1, 3, 5]:
        list3.append(data)
    list4 = LinkedList()
    for data in [2, 4, 6]:
        list4.append(data)
    print("List 1:", end=" ")
    list3.print_list()
    print("List 2:", end=" ")
    list4.print_list()
    merged_list = LinkedList.merge_sorted_lists(list3, list4)
    print("Merged sorted list:", end=" ")
    merged_list.print_list()

# Run the tests
test_linked_list()