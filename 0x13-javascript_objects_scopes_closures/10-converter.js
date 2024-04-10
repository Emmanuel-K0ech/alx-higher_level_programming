#!/usr/bin/node
/**
 * converts numbers from base 10 to another base passed argument
 */
exports.converter = function (base) {
  function myConverter (x) {
    return x.toString(base);
  }

  return myConverter;
};
