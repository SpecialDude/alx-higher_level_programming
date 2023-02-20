#!/usr/bin/node

const array = require('./100-data').list;

console.log(array);
const new_array = array.map((value, index, array) => value * index);
console.log(new_array);
