#!/usr/bin/node

let num = process.argv[2];

num = Math.floor(num);

if (Number.isInteger(num)) {
  console.log(`My number: ${num}`);
} else {
  console.log('Not a number');
}
