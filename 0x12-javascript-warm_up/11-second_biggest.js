#!/usr/bin/node

if (process.argv.length < 3 || process.argv.length === 3) console.log(0);
else {
  const first = parseInt(process.argv[2]);
  const second = parseInt(process.argv[3]);

  let biggest = (second > first) ? second : first;
  let secondBig = (second < first) ? second : first;

  for (let i = 4; i < process.argv.length; i++) {
    const item = parseInt(process.argv[i]);
    if (item > biggest) {
      secondBig = biggest;
      biggest = item;
    } else if (item > secondBig) secondBig = item;
  }

  console.log(secondBig);
}
