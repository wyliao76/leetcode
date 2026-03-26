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

describe('fib', () => {
    const fib = (n) => {
        const result = [1, 1]
        if (n === 1) {
            return [1]
        }
        if (n === 2) {
            return result
        }
        for (let i = 2; i < n; ++i) {
            result[i] = result[i - 2] + result[i - 1]
        }
        return result
    }

    it('should do fib (n)', () => {
        expect(fib(6)).toStrictEqual([
            1, 1, 2, 3, 5, 8,
        ])

        expect(fib(1)).toStrictEqual([
            1,
        ])

        expect(fib(2)).toStrictEqual([
            1, 1,
        ])
    })
})
