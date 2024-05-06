const solve = (x) => {
  return (x * (x - 1)) / 2
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
