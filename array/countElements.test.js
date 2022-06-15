function countElements(string) {
    // two pass solution
    const newString = getNewString(string)
    let currentElement = ''
    let currentCount = ''
    const dict = {}
    for (let i = 0; i < newString.length; i++) {
        if (isChar(newString[i])) {
            currentElement = currentElement + newString[i]
        } else {
            currentCount = currentCount + newString[i]
            if (isChar(newString[i + 1])) {
                dict[currentElement] = dict[currentElement] ? dict[currentElement] + Number(currentCount) : Number(currentCount)
                currentElement = ''
                currentCount = ''
            }
        }
    }
    return dict
}

const isChar = (s) => isNaN(s)

const getNewString = (string) => {
    // to turn COOH into C1O1O1H1
    // BTW my major was Chemistry and chemists are just too lazy with chemical formula

    const newString = []
    for (let i = 0; i < string.length; i++) {
        const left = string[i]
        const right = string[i + 1]
        // C1 || 1
        // just push the left to array
        if (isChar(left) && !isChar(right) || !isChar(left)) {
            newString.push(left)
        }
        // CO
        // push the left with 1 so we get C1
        if (isChar(left) && isChar(right)) {
            newString.push(left)
            newString.push('1')
        }
    }
    return newString.join('')
}


describe('playground', () => {
    it('should do countElements (1)', () => {
        const s = 'H2O'
        const expected = { 'H': 2, 'O': 1 }
        const result = countElements(s)
        expect(result).toMatchObject(expected)
    })

    it('should do countElements (2)', () => {
        const s = 'C6H12'
        const expected = { 'C': 6, 'H': 12 }
        const result = countElements(s)
        expect(result).toMatchObject(expected)
    })

    it('should do countElements (3)', () => {
        const s = 'COOH'
        const expected = { 'C': 1, 'O': 2, 'H': 1 }
        const result = countElements(s)
        expect(result).toMatchObject(expected)
    })
})
