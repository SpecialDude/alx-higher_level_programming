#!/usr/bin/node

function * numbergen () {
  let num = 0;

  while (true) {
    yield num++;
  }
}

const ngen = numbergen();

exports.logme = function (item) {
  console.log(ngen.next().value + ': ' + item);
};
