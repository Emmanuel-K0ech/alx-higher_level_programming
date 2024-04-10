#!/usr/bin/node
/**
 * sorted dictionary
 */
const dict = require('./101-data').dict;

const myDict = {};

Object.getOwnPropertyNames(dict).forEach(occurences => {
  if (myDict[dict[occurences]] === undefined) {
    myDict[dict[occurences]] = [occurences];
  } else {
    myDict[dict[occurences]].push(occurences);
  }
});
console.log(myDict);
