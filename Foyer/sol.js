function sol (list, price) {

    list = list.map(item => parseInt(item.slice(1))).sort((a, b) => a - b); //parse, and the sort the prices

    price = parseInt(price.slice(1));

    let itemsCount = 0;

    for (item of list) {
        if (item <= price) {
            itemsCount += 1; //increment the items count
            price -= item; //decrement the price
        } else {
            break;
        }
    }

    if (itemsCount === 0) {
        return "Insufficient cash!"; //if no items can be bought
    } else {
        return itemsCount; //return the number of items that can be bought
    }

}


let itemsList = [];
let totalPrice = "";
let rl = require('readline').createInterface({
    input: process.stdin
});
rl.on("line", (items) => {
    //space separated values should be introduced
    itemsList = items.split(" ");
    rl.question("", (price) => {
        totalPrice = price;
        console.log(sol(itemsList, totalPrice));
        rl.close();
    });
});