package main

import (
	"bufio"
	"fmt"
	"os"
)

func max(a, b int) int {
	if a >= b {
		return a
	}
	return b
}

func solve() {
	reader := bufio.NewReader(os.Stdin)
	var n, m, r, c int

	fmt.Fscan(reader, &n, &m, &r, &c)
	fmt.Println(max(n-r, r-1) + max(m-c, c-1))
}

func main() {
	solve()
}
