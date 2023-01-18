#!/usr/bin/node

// This Program make request to a starwars api for fetching titles

const request = require('request');

if (process.argv.length < 2) { process.exit(); }

const movieId = process.argv[2];

const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
