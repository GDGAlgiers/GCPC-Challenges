function max(a, b) {
    return a >= b ? a : b;
}

function solve() {
    const readline = require('readline');
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });

    rl.question('', input => {
        const [n, m, r, c] = input.split(' ').map(Number);
        console.log(max(n - r, r - 1) + max(m - c, c - 1));
        rl.close();
    });
}

solve();
