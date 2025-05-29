/**
 * @param {number[]} nums
 * @return {number}
 */
const firstMissingPositive = function(nums) {
    const size = nums.length
    for (let i = 0; i < size; i++) {
        while (nums[i] >= 1 && nums[i] <= size && nums[i] !== nums[nums[i] - 1]) {
            const tmp = nums[nums[i] - 1]
            nums[nums[i] - 1] = nums[i]
            nums[i] = tmp
        }
    }
    for (let i = 0; i < size; i++) {
        if (nums[i] !== i + 1) {
            return i + 1
        }
    }
    return size + 1
}


describe('playground', () => {
    it('should pass (1)', () => {
        expect(firstMissingPositive([1, 2, 0])).toBe(3)
    })

    it('should pass (2)', () => {
        expect(firstMissingPositive([3, 4, -1, 1])).toBe(2)
    })

    it('should pass (3)', () => {
        expect(firstMissingPositive([7, 8, 9, 11, 12])).toBe(1)
    })

    it('should pass (4)', () => {
        expect(firstMissingPositive([1, 3, 6, 4, 1, 2])).toBe(5)
    })

    it('should pass (5)', () => {
        expect(firstMissingPositive([1, 2, 3])).toBe(4)
    })

    it('should pass (6)', () => {
        expect(firstMissingPositive([-1, -3])).toBe(1)
    })

    it('should pass (7)', () => {
        expect(firstMissingPositive([0, 100])).toBe(1)
    })
})
