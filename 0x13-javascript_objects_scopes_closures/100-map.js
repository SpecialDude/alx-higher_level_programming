#!/usr/bin/node

const array = require('./100-data').list;

console.log(array);
const newArray = array.map((value, index, array) => value * index);
console.log(newArray);
