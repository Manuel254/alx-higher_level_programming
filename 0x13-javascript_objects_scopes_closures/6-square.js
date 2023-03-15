#!/usr/bin/node

const SquareOne = require('./5-square');

module.exports = class Square extends SquareOne {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c) {
      for (let i = 0; i < this.height; i++) {
        let pattern = '';
        for (let j = 0; j < this.width; j++) {
          pattern += c;
        }
        console.log(pattern);
      }
    } else {
      this.print();
    }
  }
};
