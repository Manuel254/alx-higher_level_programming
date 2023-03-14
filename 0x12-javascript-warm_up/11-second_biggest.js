#!/usr/bin/node

let secondBiggest;
let args = process.argv;

args.shift();
args.shift();

if (args.length === 0 || args.length === 1) {
  console.log(0);
} else {
  args = args.sort();
  secondBiggest = Math.floor(args[args.length - 2]);
  console.log(secondBiggest);
}
