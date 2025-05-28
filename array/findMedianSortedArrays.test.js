/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
const findMedianSortedArrays = function(nums1, nums2) {
    let i = 0
    let j = 0
    const nums = []
    while (i < nums1.length && j < nums2.length) {
        if (nums1[i] < nums2[j]) {
            nums.push(nums1[i])
            i++
        } else {
            nums.push(nums2[j])
            j++
        }
    }
    while (i < nums1.length) {
        nums.push(nums1[i])
        i++
    }
    while (j < nums2.length) {
        nums.push(nums2[j])
        j++
    }

    const index = Math.floor(nums.length / 2)
    if (nums.length % 2 === 0) {
        return (nums[index - 1] + nums[index]) / 2
    } else {
        return nums[index]
    }
}


describe('playground', () => {
    it('should find median (1)', () => {
        const nums1 = [1, 3]
        const nums2 = [2]
        expect(findMedianSortedArrays(nums1, nums2)).toBe(2)
    })

    it('should find median (2)', () => {
        const nums1 = [1, 2]
        const nums2 = [3, 4]
        expect(findMedianSortedArrays(nums1, nums2)).toBe(2.5)
    })
})
