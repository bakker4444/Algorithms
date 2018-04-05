// Given a singly linked list L: L0 -> L1 -> … -> Ln-1 -> Ln,
// reorder it to: L0 -> Ln -> L1 -> Ln-1 -> L2 -> Ln-2 -> …
//
// You must do this in-place without altering the nodes' values.
//
// For example,
// Given {1, 2, 3, 4}, reorder it to {1, 4, 2, 3}.

/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} head
 * @return {void} Do not return anything, modify head in-place instead.
 */

function ListNode(val) {
    this.val = val;
    this.next = null;
}

// Singly Linked List Generate (example)
var a = new ListNode(1);
var b = new ListNode(2);
a.next = b
var c = new ListNode(3);
b.next = c
var d = new ListNode(4);
c.next = d
var e = new ListNode(5);
d.next = e

console.log("BEFORE")
console.log(a)
console.log(a.next)
console.log(a.next.next)
console.log(a.next.next.next)
console.log(a.next.next.next.next)


// Singly linked list reorder function
var reorderList = function (head) {
    
    if (!head) {
        return;
    }

    var firstNode = head;
    var lastNode = head;
    
    // total number of nodes
    var numOfMoves = 1

    // find total number of nodes
    while(lastNode.next) {
        numOfMoves++;
        lastNode = lastNode.next
    }
    
    // edge cases
    if (numOfMoves == 1 || numOfMoves == 2) {
        return;
    } else if (numOfMoves == 3) {
        lastNode.next = firstNode.next;
        lastNode.next.next = null;
        firstNode.next = lastNode;
        return;
    }

    // general case
    while (numOfMoves > 3) {

        // in-place pointer change
        lastNode.next = firstNode.next;
        firstNode.next = lastNode;

        //index move
        firstNode = firstNode.next.next;
        numOfMoves = numOfMoves - 2;
        for (var i=0; i < numOfMoves; i++) {
            lastNode = lastNode.next;
        }

    }

    // last step
    if (numOfMoves == 3) {
        lastNode.next = firstNode.next;
        firstNode.next = lastNode;
        lastNode.next.next = null
    } else {
        lastNode.next = null
    }

    return;
};

console.log("================================================")
console.log("AFTER")

reorderList(a)
console.log(a)
console.log(a.next)
console.log(a.next.next)
console.log(a.next.next.next)
console.log(a.next.next.next.next)

