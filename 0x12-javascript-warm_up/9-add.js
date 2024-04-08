#!/usr/bin/node
"use strict";

let myArg = process.argv;
let num1 = parseInt(myArg[2]);
let num2 = parseInt(myArg[3]);

function add(a, b) {
    let result = a + b;
    console.log(result);
};
add(num1, num2);
