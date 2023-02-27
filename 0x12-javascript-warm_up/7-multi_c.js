#!/usr/bin/node

const argv1 = parseInt(process.argv[2]);

if (isNaN(argv1)) console.log('Missing number of occurrences');
else for (let i = 0; i < argv1; i++) console.log('C is fun');
