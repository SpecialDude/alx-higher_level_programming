#!/usr/bin/node

const argv = parseInt(process.argv[2]);

if (isNaN(argv)) console.log('Missing size');
else {
  for (let i = 0; i < argv; i++) {
    for (let j = 0; j < argv; j++) {
      process.stdout.write('X');
    }
    process.stdout.write('\n');
  }
}
