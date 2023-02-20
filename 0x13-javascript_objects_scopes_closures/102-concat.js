#!/usr/bin/node

const fs = require('fs');
const file1 = process.argv[2];
const file2 = process.argv[3];
const dest = process.argv[4];
const content1 = fs.readFileSync(`./${file1}`);
const content2 = fs.readFileSync(`./${file2}`);
fs.writeFileSync(`./${dest}`, content1 + content2);
