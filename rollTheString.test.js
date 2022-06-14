function rollTheString(s, roll) {
    // Write your code here

    // convert to Num
    const newS = s.split('').map((s) => s.charCodeAt(0))

    // find roll times for each char
    for (const timesToRoll of roll) {
        for (let i = 0; i < newS.length; i++) {
            newS[i] = i < timesToRoll ? newS[i] + 1 : newS[i]
        }
    }

    // convert back to Char
    const results = newS.map((s) => convertNumToASCII(s)).join('')
    return results
}

const convertNumToASCII = (num) => num > 122 ? String.fromCharCode(num % 123 + 97) : String.fromCharCode(num % 123)


describe('playground', () => {
    it('should do rollTheString (1)', () => {
        const s = 'abz'
        const roll = [3]
        const result = rollTheString(s, roll)
        expect(result).toBe('bca')
    })

    it('should do rollTheString (2)', () => {
        const s = 'vwxyz'
        const roll = [1, 2, 3, 4, 5]
        const result = rollTheString(s, roll)
        expect(result).toBe('aaaaa')
    })

    it('should do rollTheString (3)', () => {
        const s = 'abzz'
        const roll = [3]
        const result = rollTheString(s, roll)
        expect(result).toBe('bcaz')
    })
})
