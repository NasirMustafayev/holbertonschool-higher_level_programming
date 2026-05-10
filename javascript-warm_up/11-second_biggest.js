#!/usr/bin/node

let secondBiggest = 0;
let biggest = 0;

for (let i = 2; i < process.argv.length; i++) {
  const convert = +process.argv[i];
  if (isNaN(convert)) {
    continue;
  }
  if (convert > biggest) {
    secondBiggest = biggest;
    biggest = convert;
  } else if (convert > secondBiggest && convert !== biggest) {
    secondBiggest = convert;
  }
}

if (secondBiggest === 0) {
  console.log(0);
} else {
  console.log(secondBiggest);
}
