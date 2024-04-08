#!/usr/bin/node
'use strict';

const myArgs = process.argv;

if (myArgs[2] == null) {
  console.log('No argument');
} else {
  console.log('Argument found');
}
