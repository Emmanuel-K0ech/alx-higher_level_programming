#!/usr/bin/node
'use strict';

const myArgs = process.argv;
const integer = parseInt(myArgs[2]);

if (!isNaN(integer)) {
  console.log('My number:', integer);
} else {
  console.log('Not a number');
}
