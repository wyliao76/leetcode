/**
 * @param {string} s
 * @return {number}
 */
const lengthOfLongestSubstring = function(s) {
    let max = 0
    const dict = {}
    let left = 0

    for (let i = 0; i < s.length; i++) {
        if (dict[s[i]]) {
            left = dict[s[i]] > left ? dict[s[i]] : left
        }
        max = (i - left + 1) > max ? (i - left + 1) : max
        dict[s[i]] = i + 1
    }
    return max
}


describe('playground', () => {
    it('should do lengthOfLongestSubstring (1)', () => {
        const s = 'abcabcbb'
        const output = 3
        expect(lengthOfLongestSubstring(s)).toEqual(output)
    })

    it('should do lengthOfLongestSubstring (2)', () => {
        const s = '"bbbbb"'
        const output = 1
        expect(lengthOfLongestSubstring(s)).toEqual(output)
    })

    it('should do lengthOfLongestSubstring (3)', () => {
        const s = 'pwwkew'
        const output = 3
        expect(lengthOfLongestSubstring(s)).toEqual(output)
    })
})
