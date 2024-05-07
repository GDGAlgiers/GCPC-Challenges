function sol(net) {
	const serie = (...args) => args.reduce((acc,cur) => acc + cur, 0);
	const parallel = (...args) => 1 / (args.reduce((acc, cur) => acc + ((cur == 0) ? 0 : 1/cur), 0));
	const burned = (...args) => 0;

	return eval(net.replace(/\(/g, 'serie(').replace(/\[/g, 'parallel(').replace(/\{/g, 'burned(').replace(/\]/g, ')').replace(/\}/g, ')'));
}

//result
let rl = require('readline').createInterface({
    input: process.stdin
});

rl.on("line", (resistances) => {
	rl.close();
	console.log(sol(resistances).toFixed(2));
});
