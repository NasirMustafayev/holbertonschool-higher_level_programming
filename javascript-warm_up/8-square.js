#!/usr/bin/node

const arg = process.argv[2];
const convert = +arg;

if (isNaN(convert)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < convert; i++) {
    console.log('X'.repeat(convert));
  }
}
