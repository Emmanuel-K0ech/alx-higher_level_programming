#!/usr/bin/node
// Gets conte of a webpage and stores it in a file
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const filePath = process.argv[3];

request(url, (err, response, body) => {
  if (err) {
    return console.error('Error:', err);
  }
});
fs.writeFile(filePath, filePath, 'utf8', (err, data) => {
  if (err) {
    console.log(err);
  }
});
