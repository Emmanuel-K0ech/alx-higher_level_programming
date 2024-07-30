#!/usr/bin/node
const fs = require('fs');

const readString = fs.readFile(process.argv[2], 'utf8', (err, data) => {
  if (err) {
    return console.error(err);
  }
});
console.log(readString);
