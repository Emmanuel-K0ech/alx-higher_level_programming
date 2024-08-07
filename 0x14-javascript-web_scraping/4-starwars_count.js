#!/usr/bin/node
// Prints the number of movies where the character "Wedge Antiles"
// is present
const request = require('request');
const url = process.argv[2];
request(url, (err, response, body) => {
  if (!err) {
    const results = JSON.parse(body).results;
    console.log(results.reduce((count, movie) => {
      return movie.characters.find((character) => character.endsWith('/18/'))
        ? count + 1
        : count;
    }, 0));
  }
});
