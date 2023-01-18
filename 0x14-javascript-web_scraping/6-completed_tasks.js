#!/usr/bin/node

// This Program make request to a starwars api for fetching titles

const request = require('request');

if (process.argv.length < 3) { process.exit(); }

const url = process.argv[2];
const data = {};

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    JSON.parse(body).forEach(function (todo) {
      if (todo.completed) {
        if (data[todo.userId] === undefined) {
          data[todo.userId] = 1;
        } else {
          data[todo.userId] += 1;
        }
      }
    });

    console.log(data);
  }
});
