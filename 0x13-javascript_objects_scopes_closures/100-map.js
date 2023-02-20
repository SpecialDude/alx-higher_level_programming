#!/usr/bin/node

const array = require('./100-data').list;

const newArray = array.map((value, index, array) => value * index);
console.log(array);
console.log(newArray);
