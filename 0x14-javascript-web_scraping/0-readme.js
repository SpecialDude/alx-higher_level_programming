#!/usr/bin/node

// This Program opens a file and prints out its content

const fs = require('fs');

if (process.argv.length < 3) { process.exit(); }

const filename = process.argv[2];

fs.readFile(filename, 'utf-8', function (err, data) {
  if (err) { console.log(err); } else {
    console.log(data);
  }
});
