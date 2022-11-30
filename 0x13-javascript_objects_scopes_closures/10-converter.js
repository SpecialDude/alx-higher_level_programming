#!/usr/bin/node

const digits = ['a', 'b', 'c', 'd', 'e', 'f'];

exports.converter = function (base) {
  function convertTo (number) {
    let result = '';
    let quotient = parseInt(number / base);
    let rem = number % base;

    while (quotient > 0) {
      if (rem > 9) result = digits[rem - 10] + result;
      else result = rem + result;
      rem = quotient % base;
      quotient = parseInt(quotient / base);
    }
    if (rem > 9) result = digits[rem - 10] + result;
    else result = rem + result;
    return result;
  }

  return convertTo;
};
