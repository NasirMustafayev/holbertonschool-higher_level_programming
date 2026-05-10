#!/usr/bin/node

const arg = process.argv[2];
const convert = +arg;

if (isNaN(convert)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + convert);
}
