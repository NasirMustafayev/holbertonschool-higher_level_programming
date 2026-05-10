#!/usr/bin/node

function add (a, b) {
  return a + b;
}

const arg1 = process.argv[2];
const arg2 = process.argv[3];
const convert1 = +arg1;
const convert2 = +arg2;

if (isNaN(convert1) || isNaN(convert2)) {
  console.log('NaN');
} else {
  console.log(add(convert1, convert2));
}
