/**
 * @param {number} a
 * @param {number} b
 * @return {number}
 */
const getSum = function(a, b) {
    while (b !== 0) {
        const carry = (a & b) << 1
        a = a ^ b
        b = carry
    }
    return a
}


describe('playground', () => {
    it('should pass (1)', () => {
        expect(getSum(1, 2)).toBe(3)
    })

    it('should pass (2)', () => {
        expect(getSum(2, 3)).toBe(5)
    })

    it('should pass (3)', () => {
        expect(getSum(-1, 1)).toBe(0)
    })
})
