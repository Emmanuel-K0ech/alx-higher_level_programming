#!/usr/bin/node
// Displays the status code of a GET request : code: <status code>
const myRequest = new Request(process.argv[2]);

fetch(myRequest)
  .then((response) => {
    console.log(`code: ${response.status}`);
  })
  .catch((error) => {
    console.error('Error', error);
  });
