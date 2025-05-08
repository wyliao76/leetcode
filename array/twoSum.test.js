
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */

const twoSum = (nums, target) => {
    // // two pass
    // const dict = {}
    // for (let i = 0; i < nums.length; i++) {
    //     dict[nums[i]] = i
    // }
    // for (let i = 0; i < nums.length; i++) {
    //     const remainder = target - nums[i]
    //     if (dict[remainder] !== undefined && dict[remainder] !== i) {
    //         return [i, dict[remainder]]
    //     }
    // }
    // return []

    // // one pass
    // const dict = {}
    // for (let i = 0; i < nums.length; i++) {
    //     const remainder = target - nums[i]
    //     if (dict[remainder] !== undefined) {
    //         return [i, dict[remainder]]
    //     }
    //     dict[nums[i]] = i
    // }
    // return []

    // why not just use array?
    const remainders = []
    for (let i = 0; i < nums.length; i++) {
        const remainder = target - nums[i]
        if (remainders.includes(nums[i])) {
            return [nums.indexOf(remainder), i]
        }
        remainders.push(remainder)
    }
    return []
}

describe('playground', () => {
    it('should do twoSum (1)', () => {
        const nums = [2, 7, 11, 15]
        const target = 9
        expect(twoSum(nums, target).sort()).toEqual([0, 1])
    })

    it('should do twoSum (2)', () => {
        const nums = [3, 2, 4]
        const target = 6
        expect(twoSum(nums, target).sort()).toEqual([1, 2])
    })

    it('should do twoSum (3)', () => {
        const nums = [3, 3]
        const target = 6
        expect(twoSum(nums, target).sort()).toEqual([0, 1])
    })
})
