## 146. LRU Cache
#
# Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.
#
#     * get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
#     * put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.
#
# Follow up:
#     Could you do both operations in O(1) time complexity?
#
# Example:
#     LRUCache cache = new LRUCache( 2 /* capacity */ );
#
#     cache.put(1, 1);
#     cache.put(2, 2);
#     cache.get(1);       // returns 1
#     cache.put(3, 3);    // evicts key 2
#     cache.get(2);       // returns -1 (not found)
#     cache.put(4, 4);    // evicts key 1
#     cache.get(1);       // returns -1 (not found)
#     cache.get(3);       // returns 3
#     cache.get(4);       // returns 4
##


## Leetcode Hard, Design question
## amazon phone interview design questions. 2019-02-11
# reference : https://www.youtube.com/watch?v=R0GTqg3pJKg
class Node(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class LRUCache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.dict = dict()
        self.head, self.tail = Node(0, 0), Node(0, 0)
        self.head.next, self.tail.prev = self.tail, self.head

    def get(self, key):
        if key not in self.dict:
            return -1
        node = self.dict[key]
        self._remove(node)
        self._add(node)
        return node.value

    def put(self, key, value):
        if key in self.dict:
            self._remove(self.dict[key])
        node = Node(key, value)
        self._add(node)
        self.dict[key] = node
        if len(self.dict) > self.capacity:
            node = self.head.next
            self._remove(node)
            del self.dict[node.key]

    def _add(self, node):
        last_node = self.tail.prev
        last_node.next = node
        self.tail.prev = node
        node.prev = last_node
        node.next = self.tail

    def _remove(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def printNode(self):
        result = ""
        result = result + "[old] -> "
        node = self.head.next
        while node != self.tail:
            result += str(node.value) + " "
            node = node.next
        result = result + "<- [new]"
        print(result)



if __name__ == "__main__":
    test_input = ["LRUCache","put","put","get","put","get","put","get","get","get"]
    test_variables = [[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]

    for i in range(len(test_input)):
        if test_input[i] == "LRUCache":
            print("Creating object")
            obj = LRUCache(test_variables[i][0])
        elif test_input[i] == "put":
            print("put", test_variables[i][1])
            obj.put(test_variables[i][0], test_variables[i][1])
        else:   # get case
            print("get", test_variables[i][0])
            print(obj.get(test_variables[i][0]))
        obj.printNode()
