#!/usr/bin/node

// This Program make request to a starwars api for fetching all characters

const request = require('request-promise');

if (process.argv.length < 3) { process.exit(); }

const movieId = process.argv[2];

const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, async function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const characters = JSON.parse(body).characters;

    for (let i = 0; i < characters.length; i++) {
      await request(characters[i], function (error, response, body) {
        if (error) {
          console.log(error);
        } else {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});
