#!/usr/bin/node
"use strict";

let myArgs = process.argv;
let integer = parseInt(myArgs[2]);
let i = 0;

if (isNaN(integer)) {
    console.log("Missing number of occurrences");
}
while (i < integer) {
    console.log("C is fun");
    i++;
}
