#!/usr/bin/node

const list = require('./100-data').list;

console.log(list);
let counter = 0;

console.log(list.map(function (x) {
  return x * counter++;
}));
