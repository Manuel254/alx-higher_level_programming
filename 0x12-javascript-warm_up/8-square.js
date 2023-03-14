#!/usr/bin/node

const arg = Math.floor(process.argv[2]);
let pattern;

if (Number.isInteger(arg)) {
  for (let i = 0; i < arg; i++) {
    pattern = '';
    for (let j = 0; j < arg; j++) {
      pattern += 'X';
    }
    console.log(pattern);
  }
} else {
  console.log('Missing size');
}
