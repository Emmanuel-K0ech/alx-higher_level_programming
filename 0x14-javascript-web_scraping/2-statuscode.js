#!/usr/bin/node
// Displays the status code of a GET request : code: <status code>
const request = require('request');
request.get(process.argv[2]).on('response', (response) => {
  console.log(`code: ${response.statusCode}`);
});
