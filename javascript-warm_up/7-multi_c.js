#!/usr/bin/node

const arg = process.argv[2];
const convert = +arg;

if (isNaN(convert)) {
  console.log('Missing number of occurrences');
} else {
  let i = 0;
  while (i < convert) {
    console.log('C is fun');
    i++;
  }
}
