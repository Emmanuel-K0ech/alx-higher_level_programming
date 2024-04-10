#!/usr/bin/node
/**
 * using array.map and arrow functions
 */
const list = require('./100-data.js').list;

const mapList = list.map((element, index) => element * index);
console.log(list);
console.log(mapList);
