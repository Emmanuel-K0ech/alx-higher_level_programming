#!/usr/bin/node
'use strict';

const myArg = process.argv;
const num1 = parseInt(myArg[2]);
const num2 = parseInt(myArg[3]);

function add (a, b) {
  const result = a + b;
  console.log(result);
}
add(num1, num2);
