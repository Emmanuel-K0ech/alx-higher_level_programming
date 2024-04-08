#!/usr/bin/node
"use strict";

let myArg = process.argv;
let integer = parseInt(myArg[2]);

function factorial(x) {
    //Base case: x == NaN or x < 0
    if (isNaN(x) || x < 0) {
        return 1;
    }

    //Base case: x === 0
    if (x === 0) {
        return 1;
    }

    // Recursive multiplication
    return x * factorial(x - 1);
};

console.log(factorial(integer));
