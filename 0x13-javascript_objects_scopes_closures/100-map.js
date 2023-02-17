#!/usr/bin/node

const array = require('./100-data').list;

console.log(array);
let counter = 0;

console.log(array.map(function (x) {
  return x * counter++;
}));
