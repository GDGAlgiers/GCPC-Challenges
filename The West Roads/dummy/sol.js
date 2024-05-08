const solve = (x) => {
  let sum = 0
  for (let i = 1; i < x; i++) {
    sum += i
  }
  return sum
}

const readline = require('readline').createInterface({
  input: process.stdin,
})

const input = []
let index = 0
const limit = 1

readline.on('line', (line) => {
  input.push(line)
  index++
  if (index == limit) {
    readline.close()
    const x = parseInt(input[0])
    console.log(solve(x))
  }
})
