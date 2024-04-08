#!/usr/bin/node
"use strict";

let myArg = parseInt(process.argv[2]);
let result = parseInt(myArg);
let sec_result = 0;

for (let i = 3; i < process.argv.length; i++)
{
    let current = parseInt(process.argv[i]);
    if (!isNaN(current) && current > result) {
        sec_result = result;
        result = current;
    }
}
console.log(sec_result);
