#!/usr/bin/node

// This Program make request to a starwars api for fetching titles

const request = require('request');

if (process.argv.length < 2) { process.exit(); }

const url = process.argv[2];
const wedgeId = 18;
let movieCount = 0;

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    JSON.parse(body).results.forEach(function (value) {
      value.characters.forEach(function (charac) {
        const parts = charac.split('/');
        const id = parseInt(parts[parts.length - 2]);

        if (id === wedgeId) movieCount++;
      });
    });
    console.log(movieCount);
  }
});
