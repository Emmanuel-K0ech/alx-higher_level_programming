#!/usr/bin/node
// Prints title of a Star Wars movie where episode
// number matches a given integer
const request = require('request');
const API_URL = 'https://swapi-api.alx-tools.com/api/films/';
const numEpisode = process.argv[2];

request(API_URL + numEpisode, (err, response, body) => {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const responseJSON = JSON.parse(body);
    console.log(responseJSON.title);
  } else {
    console.log('Error code: ' + response.statusCode);
  }
});
