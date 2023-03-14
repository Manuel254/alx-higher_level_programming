#!/usr/bin/node

const firstNum = Math.floor(process.argv[2]);
const secondNum = Math.floor(process.argv[3]);

function add (a, b) {
  return a + b;
}

const result = add(firstNum, secondNum);

console.log(result);
