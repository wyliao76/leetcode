function rollTheString(s, roll) {
    // Write your code here
    // create a lookup table
    const alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    const dict = {}
    for (let i = 0; i < alphabets.length; i++) {
        dict[alphabets[i]] = alphabets[i + 1] || alphabets[0]
    }

    let newString = s
    for (let i = 0; i < roll.length; i++) {
        const toRoll = newString.substring(0, roll[i])
        const notToRoll = newString.substring(roll[i])

        let rolledSubStrings = []
        for (let j = 0; j < roll[i]; j++) {
            rolledSubStrings.push(dict[toRoll[j]])
        }
        const rolled = rolledSubStrings.join('')
        newString = rolled + notToRoll
        rolledSubStrings = []
    }
    return newString
}

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
})
