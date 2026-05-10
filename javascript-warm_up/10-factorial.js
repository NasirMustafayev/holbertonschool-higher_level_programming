#!/usr/bin/node

function factorial (n) {
  if (n === 0 || n === 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

const arg = process.argv[2];
const convert = +arg;

if (isNaN(convert) || convert < 0) {
  console.log('NaN');
} else {
  console.log(factorial(convert));
}
