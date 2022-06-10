function fizzBuzz(n) {
    // Write your code here
    const results = []
    for (let i = 1; i < n + 1; i++) {
        switch (true) {
        case (i % 3 === 0 && i % 5 === 0):
            results.push('FizzBuzz')
            break
        case (i % 3 === 0):
            results.push('Fizz')
            break
        case (i % 5 === 0):
            results.push('Buzz')
            break
        default:
            results.push(String(i))
        }
    }
    return results
}


describe('playground', () => {
    it('should do fizzBuzz (1)', () => {
        const n = 15
        const result = fizzBuzz(n)
        expect(result).toStrictEqual([
            '1',
            '2',
            'Fizz',
            '4',
            'Buzz',
            'Fizz',
            '7',
            '8',
            'Fizz',
            'Buzz',
            '11',
            'Fizz',
            '13',
            '14',
            'FizzBuzz',
        ])
    })
})
