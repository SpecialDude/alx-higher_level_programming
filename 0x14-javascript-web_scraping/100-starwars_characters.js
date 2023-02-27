#!/usr/bin/node

// This Program make request to a starwars api for fetching all characters

const request = require('request');

if (process.argv.length < 3) { process.exit(); }

const movieId = process.argv[2];

const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    JSON.parse(body).characters.forEach(function (charURL) {
      request(charURL, function (error, response, body) {
        if (error) {
          console.log(error);
        } else {
          console.log(JSON.parse(body).name);
        }
      });
    });
  }
});
