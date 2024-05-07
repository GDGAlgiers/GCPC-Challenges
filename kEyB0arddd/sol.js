function sol(str) {
    
    let words = str.replace(/Ctrl \+ (C|X|V)/g, (match, p1) => '#' + p1.toLowerCase()).split(" ");
    let out = "";
    let copied = "";

    for (let i = 0; i < words.length; i++) {
        switch (words[i]) {
            case "#c":
                copied = out;
                break;
            case "#v":
                out += copied;
                break;
            case "#x":
                copied = out.slice(0, i < words.length - 1 ? undefined : -1);
                out = ""
                break;
            default:
                out += words[i] + (i < words.length - 1 ? " " : "");
        }
    }

    return out;
}

//result
let rl = require('readline').createInterface({
    input: process.stdin
});

rl.on("line", (inline) => {
	rl.close();
	console.log(sol(inline));
});
