#!/usr/bin/node

const fs = require('fs');
const request = require('request');
const url = process.argv[2];
const filename = process.argv[3];

request
  .get(url)
  .on('error', function (err) {
    console.error(err);
  })
  .pipe(fs.createWriteStream(filename));
