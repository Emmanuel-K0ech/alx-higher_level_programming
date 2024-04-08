#!/usr/bin/node
"use strict";

let myArgs = process.argv;
let integer = parseInt(myArgs[2]);

if (!isNaN(integer)) {
    console.log("My number: ", integer);
} else {
    console.log("Not a number");
}
