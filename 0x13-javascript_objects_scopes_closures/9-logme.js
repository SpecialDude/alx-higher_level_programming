#!/usr/bin/node

let counter = 0;

exports.logme = function (item) {
  console.log(`${counter}: ${item}`);
  counter++;
};
