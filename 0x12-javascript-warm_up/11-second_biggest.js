#!/usr/bin/node

let secondBiggest;
const args = process.argv;

args.shift();
args.shift();

if (args.length === 0 || args.length === 1) {
  console.log('0');
} else {
  args.sort((a, b) => a - b);
  secondBiggest = args[args.length - 2];
  console.log(secondBiggest);
}
