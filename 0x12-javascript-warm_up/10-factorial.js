#!/usr/bin/node

const number = Math.floor(process.argv[2]);

function factorial (num) {
  if (num === 0 || num === 1 || isNaN(num)) { return 1; }
  return num * factorial(num - 1);
}

console.log(factorial(number));
