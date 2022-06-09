/**
 * @param {number[]} height
 * @return {number}
 */
const trap = function(height) {
    //        *
    //    *&&&**&*
    // **&**&******

    // find the peak
    let peak = 0
    let peakIndex = 0
    for (const index in height) {
        if (height[index] > peak) {
            peak = height[index]
            peakIndex = index
        }
    }

    // go from left to peak
    let total = 0
    let leftMax = 0
    let rightMax = 0
    for (let i = 0; i < peakIndex; i++) {
        if (height[i] > leftMax) {
            leftMax = height[i]
        } else {
            total += leftMax - height[i]
        }
    }

    // go from right to peak
    for (let i = height.length - 1; i > peakIndex; i--) {
        if (height[i] > rightMax) {
            rightMax = height[i]
        } else {
            total += rightMax - height[i]
        }
    }
    return total
}

describe('playground', () => {
    it('should do trap (1)', () => {
        const height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
        const output = 6
        expect(trap(height)).toEqual(output)
    })

    it('should do trap (2)', () => {
        const height = [4, 2, 0, 3, 2, 5]
        const output = 9
        expect(trap(height)).toEqual(output)
    })
})
