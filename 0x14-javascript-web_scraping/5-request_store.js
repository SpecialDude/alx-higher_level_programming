#!/usr/bin/node

// This Program opens a file and write response body to it

const fs = require('fs');
const request = require('request');

if (process.argv.length < 4) { process.exit(1); }

const url = process.argv[2];
const filename = process.argv[3];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
    process.exit(1);
  } else {
    fs.writeFile(filename, body, 'utf-8', function (err) {
      if (err) { console.log(err); }
    });
  }
});
