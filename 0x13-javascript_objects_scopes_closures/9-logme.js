#!/usr/bin/node

let count = 0;

exports.logme = function (item) {
  console.log(`${count}: ${item}`);
  count++;
};
