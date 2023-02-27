#!/usr/bin/node

// This Program opens a file and write into it

const fs = require('fs');

if (process.argv.length < 4) { process.exit(); }

const filename = process.argv[2];
const content = process.argv[3];

fs.writeFile(filename, content, 'utf-8', function (err) {
  if (err) { console.log(err); }
});
