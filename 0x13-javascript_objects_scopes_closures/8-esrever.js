#!/usr/bin/node
/**
 * function to reverse a list
 */
exports.esrever = function (list) {
  const reversedList = [];
  const len = list.length;
  let i = 0;

  for (i = len - 1; i >= 0; i--) {
    reversedList.push(list[i]);
  }
  return reversedList;
};
