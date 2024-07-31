#!/usr/bin/node
// Prints all characters of a Star Wars movie
const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/';
request.get(url + id, (err, response, body) => {
  if (err) {
    console.log(err);
  }
  const data = JSON.parse(body);
  const dataString = data.characters;
  for (const x of dataString) {
    request.get(x, (err, response, body1) => {
      if (err) {
        console.log(err);
      }
      const data1 = JSON.parse(body1);
      console.log(data1.name);
    });
  }
});
