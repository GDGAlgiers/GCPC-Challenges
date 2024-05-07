const digitEquivalent = {
    "0": ["0", "8"],
    "1": ["1", "2", "4"],
    "2": ["1", "2", "3", "5"],
    "3": ["2", "3", "6"],
    "4": ["1", "4", "5", "7"],
    "5": ["2", "4", "5", "6", "8"],
    "6": ["3", "5", "6", "9"],
    "7": ["4", "7", "8"],
    "8": ["0", "5", "7", "8", "9"],
    "9": ["6", "8", "9"]
}

function SecretAgent(pin) {
    var arr = [],
        comb = [];

    for (var i = pin.length - 1; i >= 0; i--) {
        arr = digitEquivalent[pin.charAt(i)];
        comb = getCombinations(arr, comb);
    }

    return comb.join(" ");
}

function getCombinations(arr1, arr2) {
    var combination = [];

    if (arr1.length == 0) return arr2;
    if (arr2.length == 0) return arr1;

    for (var i = 0; i < arr1.length; i++) {
        for (var j = 0; j < arr2.length; j++) {
            combination.push(arr1[i] + arr2[j]);
        }
    }

    return combination;
}

result
let rl = require('readline').createInterface({
    input: process.stdin
});

rl.on("line", (code) => {
	rl.close();
	console.log(SecretAgent(code));
});
