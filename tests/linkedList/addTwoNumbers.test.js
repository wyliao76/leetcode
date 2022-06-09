//  * Definition for singly-linked list.
function ListNode(val, next) {
    this.val = (val === undefined ? 0 : val)
    this.next = (next === undefined ? null : next)
}

/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
const addTwoNumbers = function(l1, l2) {
    // init new node
    const result = new ListNode(0)
    let resultTail = result
    let carry = 0
    while (l1 || l2) {
        const val1 = l1 ? l1.val : 0
        const val2 = l2 ? l2.val : 0
        const sum = carry + val1 + val2
        // add 1 to carry if sum exceed 10
        carry = sum >= 10 ? 1 : 0
        // init new node for sum and assign to next
        resultTail.next = new ListNode(sum % 10)
        // advance current
        resultTail = resultTail.next
        // advance l1 & l2
        if (l1) l1 = l1.next
        if (l2) l2 = l2.next
    }
    // add new node if still has a carry after l1 & l2 are done
    if (carry === 1) {
        resultTail.next = new ListNode(carry)
    }
    // return nodes after the 0 one
    return result.next
}

function getListNodeFromArray(array) {
    let current
    for (let i = array.length - 1; i > -1; i--) {
        current = current ? new ListNode(array[i], current) : new ListNode(array[i])
    }
    return current
}

describe('playground', () => {
    it('should do addTwoNumbers (1)', () => {
        const l1 = getListNodeFromArray([2, 4, 3])
        const l2 = getListNodeFromArray([5, 6, 4])
        const output = getListNodeFromArray([7, 0, 8])
        expect(addTwoNumbers(l1, l2)).toEqual(output)
    })

    it('should do addTwoNumbers (2)', () => {
        const l1 = getListNodeFromArray([0])
        const l2 = getListNodeFromArray([0])
        const output = getListNodeFromArray([0])
        expect(addTwoNumbers(l1, l2)).toEqual(output)
    })

    it('should do addTwoNumbers (3)', () => {
        const l1 = getListNodeFromArray([9, 9, 9, 9, 9, 9, 9])
        const l2 = getListNodeFromArray([9, 9, 9, 9])
        const output = getListNodeFromArray([8, 9, 9, 9, 0, 0, 0, 1])
        expect(addTwoNumbers(l1, l2)).toEqual(output)
    })
})
