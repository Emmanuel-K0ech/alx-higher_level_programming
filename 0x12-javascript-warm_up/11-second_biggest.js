#!/usr/bin/node
'use strict';

const myArg = parseInt(process.argv[2]);
let result = parseInt(myArg);
let secResult = 0;

for (let i = 3; i < process.argv.length; i++) {
  const current = parseInt(process.argv[i]);
  if (!isNaN(current) && current > result) {
    secResult = result;
    result = current;
  }
}
console.log(secResult);
