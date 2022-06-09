/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
const topKFrequent = (nums, k) => {
    // make a dict
    const dict = {}
    for (const num of nums) {
        dict[num] = dict[num] ? dict[num] + 1 : 1
    }

    // get a sorted objectArray
    const objectArray = []
    for (const key of Object.keys(dict)) {
        objectArray.push([key, dict[key]])
    }
    // sort from largest
    const sortedObjectArray = objectArray.sort((a, b) => b[1] - a[1])

    // get topK array
    const topK = []
    for (let i = 0; i < k; i++) {
        topK.push(Number(sortedObjectArray[i][0]))
    }
    return topK
}

describe('playground', () => {
    it('should do top K Frequent Elements (1)', () => {
        const nums = [1, 1, 1, 2, 2, 3]
        const k = 2
        expect(topKFrequent(nums, k).sort()).toEqual([1, 2])
    })

    it('should do top K Frequent Elements (2)', () => {
        const nums = [1]
        const k = 1
        expect(topKFrequent(nums, k).sort()).toEqual([1])
    })

    it('should do top K Frequent Elements (3)', () => {
        const nums = [-1, -1]
        const k = 1
        expect(topKFrequent(nums, k).sort()).toEqual([-1])
    })
})
