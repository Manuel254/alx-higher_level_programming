#!/usr/bin/node

const firstNum = Math.floor(process.argv[2]);
const secondNum = Math.floor(process.argv[3]);
let result;

function add (a, b) {
  return a + b;
}

result = add(firstNum, secondNum);

console.log(result);
