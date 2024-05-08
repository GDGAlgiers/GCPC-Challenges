function max(a, b) {
  return a >= b ? a : b;
}

function solve(input) {
  const [n, m, r, c] = input.split(" ").map(Number);
  console.log(max(n - r, r - 1) + max(m - c, c - 1));
}

let rl = require("readline").createInterface({
  input: process.stdin,
});

rl.on("line", (input) => {
  solve(input);
  rl.close();
});
