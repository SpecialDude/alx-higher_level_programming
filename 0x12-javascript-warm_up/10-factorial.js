#!/usr/bin/node

function factorial (num) {
  if (isNaN(num) || num === 0 || num === 1) return 1;
  else return num * factorial(num - 1);
}

const argv = process.argv[2];

console.log(factorial(argv));
