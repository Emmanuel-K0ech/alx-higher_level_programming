#!/usr/bin/node
// Gets conte of a webpage and stores it in a file
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const filePath = process.argv[3];
request(url).pipe(fs.createWriteStream(filePath));
