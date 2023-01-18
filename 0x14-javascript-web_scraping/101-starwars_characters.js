#!/usr/bin/node

// This Program make request to a starwars api for fetching all characters

const request = require('request-promise-native');

if (process.argv.length < 3) { process.exit(); }

const movieId = process.argv[2];

const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

async function printName (url) {
  await request(url, function (error, response, body) {
    if (error) {
      console.log(error);
    } else {
      console.log(JSON.parse(body).name);
    }
  });
}

function loadURL (urlList) {
  for (let i = 0; i < urlList.length; i++) {
    printName(urlList[i]);
  }
}

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const characters = JSON.parse(body).characters;

    loadURL(characters);
  }
});
