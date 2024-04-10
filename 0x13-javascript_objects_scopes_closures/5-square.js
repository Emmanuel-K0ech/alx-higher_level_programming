#!/usr/bin/node
/**
 * New class square
 */
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size); // size works as w & h
  }
}

module.exports = Square;
