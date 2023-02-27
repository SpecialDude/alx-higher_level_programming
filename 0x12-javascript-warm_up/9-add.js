#!/usr/bin/node

function add (a, b) {
  console.log(a + b);
}

const argv1 = parseInt(process.argv[2]);
const argv2 = parseInt(process.argv[3]);

add(argv1, argv2);
