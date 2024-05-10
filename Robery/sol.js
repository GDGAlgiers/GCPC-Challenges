const solve = (x, y, n_row, n_col, maze, visit) => {
  visit[x][y] = 1
  if (x === 0 || x === n_row - 1 || y === 0 || y === n_col - 1) {
    //check if current position is possible escape
    return `${x},${y}`
  }
  if (maze[x - 1][y] === '1' && visit[x - 1][y] === 0) {
    //check if element on top is free and not visited
    const neighborEscape = solve(x - 1, y, n_row, n_col, maze, visit)
    if (neighborEscape) {
      return `${x},${y}-${neighborEscape}`
    }
  }
  if (maze[x][y + 1] === '1' && visit[x][y + 1] === 0) {
    //check if element on right is free and not visited
    const neighborEscape2 = solve(x, y + 1, n_row, n_col, maze, visit)
    if (neighborEscape2) {
      return `${x},${y}-${neighborEscape2}`
    }
  }
  if (maze[x + 1][y] === '1' && visit[x + 1][y] === 0) {
    //check if element under is free and not visited
    const neighborEscape3 = solve(x + 1, y, n_row, n_col, maze, visit)
    if (neighborEscape3) {
      return `${x},${y}-${neighborEscape3}`
    }
  }
  if (maze[x][y - 1] === '1' && visit[x][y - 1] === 0) {
    //check if element on left is free and not visited
    const neighborEscape4 = solve(x, y - 1, n_row, n_col, maze, visit)
    if (neighborEscape4) {
      return `${x},${y}-${neighborEscape4}`
    }
  }
  return ''
}

const readline = require('readline').createInterface({
  input: process.stdin,
})

const input = []
let index = 0
const limit = 5

readline.on('line', (line) => {
  input.push(line)
  index++
  if (index == limit) {
    readline.close()
    const n_row = parseInt(input[0])
    const n_col = parseInt(input[1])
    const x0 = parseInt(input[3])
    const y0 = parseInt(input[4])
    maze = []
    input_maze = input[2].split(' ')
    for (let i = 0; i < n_row; i++) {
      maze.push(input_maze.slice(i * n_col, (i + 1) * n_col))
    }
    visit = new Array(n_row).fill().map(() => new Array(n_col).fill(0))
    console.log(solve(x0, y0, n_row, n_col, maze, visit))
  }
})
