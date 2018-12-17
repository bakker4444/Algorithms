## 138. Copy List with Random Pointer
#
# A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.
#
# Return a deep copy of the list.
##


# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


##################################
## IMPORTANT CONCEPT!
## how to do deep copy( like A = new SomeClass_or_Objects(), located @Heap_memory )
## and swallow copy ( like newVariable = oldVariable, located @stack_memory )
##################################


## reference
## https://leetcode.com/problems/copy-list-with-random-pointer/discuss/43485/Clear-and-short-python-O(2n)-and-O(n)-solution
## O(2n)
from collections import defaultdict
class Solution1(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        dict2 = dict()
        node = head
        while node:
            dict2[node] = RandomListNode(node.label)
            node = node.next
        node = head
        while node:
            dict2[node].next = dict2.get(node.next)
            dict2[node].random = dict2.get(node.random)
            node = node.next
        return dict2.get(head)


## reference
## https://leetcode.com/problems/copy-list-with-random-pointer/discuss/43485/Clear-and-short-python-O(2n)-and-O(n)-solution
## O(n), using defaultdict()
class Solution2(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        dict1 = defaultdict(lambda: RandomListNode(0))
        dict1[None] = None
        n = head
        while n:
            dict1[n].label = n.label
            dict1[n].next = dict1[n.next]
            dict1[n].random = dict1[n.random]
            n = n.next
        return dict1[head]


## recursive approach, like graph
## time : O(N),     space : O(N), asymptotically
## reference, Approach 1: Recursive
## https://leetcode.com/problems/copy-list-with-random-pointer/solution/
class Solution3(object):
    """
    :type head: RandomListNode
    :rtype: RandomListNode
    """
    def __init__(self):
        # Dictionary which holds old nodes as keys and new nodes as its values.
        self.visitedHash = {}

    def copyRandomList(self, head):

        if head == None:
            return None

        # If we have already processed the current node, then we simply return the cloned version of it.
        if head in self.visitedHash:
            return self.visitedHash[head]

        # create a new node
        # with the label same as old node.
        node = RandomListNode(head.label)

        # Save this value in the hash map. This is needed since there might be
        # loops during traversal due to randomness of random pointers and this would help us avoid them.
        self.visitedHash[head] = node

        # Recursively copy the remaining linked list starting once from the next pointer and then from the random pointer.
        # Thus we have two independent recursive calls.
        # Finally we update the next and random pointers for the new node created.
        node.next = self.copyRandomList(head.next)
        node.random = self.copyRandomList(head.random)

        return node


## Iterative approach using dictionary
## time : O(N),     space : O(N)
## reference, Approach 2: Iterative with O(N) space
## https://leetcode.com/problems/copy-list-with-random-pointer/solution/
class Solution4(object):
    def __init__(self):
        # Creating a visited dictionary to hold old node reference as "key" and new node reference as the "value"
        self.visited = {}

    def getClonedNode(self, node):
        # If node exists then
        if node:
            # Check if its in the visited dictionary
            if node in self.visited:
                # If its in the visited dictionary then return the new node reference from the dictionary
                return self.visited[node]
            else:
                # Otherwise create a new node, save the reference in the visited dictionary and return it.
                self.visited[node] = RandomListNode(node.label)
                return self.visited[node]
        return None

    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """

        if not head:
            return head

        old_node = head
        # Creating the new head node.
        new_node = RandomListNode(old_node.label)
        self.visited[old_node] = new_node

        # Iterate on the linked list until all nodes are cloned.
        while old_node != None:

            # Get the clones of the nodes referenced by random and next pointers.
            new_node.random = self.getClonedNode(old_node.random)
            new_node.next = self.getClonedNode(old_node.next)

            # Move one step ahead in the linked list.
            old_node = old_node.next
            new_node = new_node.next

        return self.visited[head]


## iterative approach with O(1) space
## time : O(N),     space : O(1)
## reference, Approach 3: Iterative with O(1) Space
## https://leetcode.com/problems/copy-list-with-random-pointer/solution/
class Solution5(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return head

        # Creating a new weaved list of original and copied nodes.
        ptr = head
        while ptr:

            # Cloned node
            new_node = RandomListNode(ptr.label)

            # Inserting the cloned node just next to the original node.
            # If A->B->C is the original linked list,
            # Linked list after weaving cloned nodes would be A->A'->B->B'->C->C'
            new_node.next = ptr.next
            ptr.next = new_node
            ptr = new_node.next

        ptr = head

        # Now link the random pointers of the new nodes created.
        # Iterate the newly created list and use the original nodes random pointers,
        # to assign references to random pointers for cloned nodes.
        while ptr:
            ptr.next.random = ptr.random.next if ptr.random else None
            ptr = ptr.next.next

        # Unweave the linked list to get back the original linked list and the cloned list.
        # i.e. A->A'->B->B'->C->C' would be broken to A->B->C and A'->B'->C'
        ptr_old_list = head # A->B->C
        ptr_new_list = head.next # A'->B'->C'
        head_old = head.next
        while ptr_old_list:
            ptr_old_list.next = ptr_old_list.next.next
            ptr_new_list.next = ptr_new_list.next.next if ptr_new_list.next else None
            ptr_old_list = ptr_old_list.next
            ptr_new_list = ptr_new_list.next
        return head_old



if __name__ == "__main__":
    a1 = RandomListNode(1)
    a2 = RandomListNode(2)
    a3 = RandomListNode(3)
    a4 = RandomListNode(4)
    a5 = RandomListNode(5)
    a1.next, a1.random = a2, a4
    a2.next, a2.random = a3, a1
    a3.next, a3.random = a4, a2
    a4.next, a4.random = a5, a5
    a5.random = a3

    results, count = [], 1
    results.append(Solution1().copyRandomList(a1))
    results.append(Solution2().copyRandomList(a1))
    results.append(Solution3().copyRandomList(a1))
    results.append(Solution4().copyRandomList(a1))
    results.append(Solution5().copyRandomList(a1))

    for result in results:
        print("====== Solution", count, "======")
        count+=1
        node = result
        while node:
            print(node.label, node.random.label)
            node = node.next
