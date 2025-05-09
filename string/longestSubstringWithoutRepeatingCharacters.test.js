/**
 * @param {string} s
 * @return {number}
 */
const lengthOfLongestSubstring = function(s) {
    let max = 0
    const substring = []

    for (let i = 0; i < s.length; i++) {
        if (substring.includes(s[i])) {
            const index = substring.indexOf(s[i]) + 1
            for (let i = 0; i < index; i++) {
                substring.shift()
            }
        }
        substring.push(s[i])
        if (substring.length > max) {
            max = substring.length
        }
    }
    return max

    // let max = 0
    // const dict = {}
    // let left = 0

    // for (let i = 0; i < s.length; i++) {
    //     if (dict[s[i]]) {
    //         left = dict[s[i]] > left ? dict[s[i]] : left
    //     }
    //     max = (i - left + 1) > max ? (i - left + 1) : max
    //     dict[s[i]] = i + 1
    // }
    // return max
}

describe('playground', () => {
    it('should do lengthOfLongestSubstring (1)', () => {
        const s = 'abcabcbb'
        const output = 3
        expect(lengthOfLongestSubstring(s)).toEqual(output)
    })

    it('should do lengthOfLongestSubstring (2)', () => {
        const s = 'bbbbb'
        const output = 1
        expect(lengthOfLongestSubstring(s)).toEqual(output)
    })

    it('should do lengthOfLongestSubstring (3)', () => {
        const s = 'pwwkew'
        const output = 3
        expect(lengthOfLongestSubstring(s)).toEqual(output)
    })

    it('should do lengthOfLongestSubstring (4)', () => {
        const s = ' '
        const output = 1
        expect(lengthOfLongestSubstring(s)).toEqual(output)
    })

    it('should do lengthOfLongestSubstring (5)', () => {
        const s = 'dvdf'
        const output = 3
        expect(lengthOfLongestSubstring(s)).toEqual(output)
    })

    it('should do lengthOfLongestSubstring (6)', () => {
        const s = 'aabaab!bb'
        const output = 3
        expect(lengthOfLongestSubstring(s)).toEqual(output)
    })
})
