#!/usr/bin/node

counter = 0;

exports.logme = function (item) {
  console.log(`${counter}: ${item}`);
  counter++;
};
