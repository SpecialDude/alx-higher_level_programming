#!/usr/bin/node

// This Program make request to a url and prints the response status

const request = require('request');

if (process.argv.length < 2) { process.exit(); }

const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
