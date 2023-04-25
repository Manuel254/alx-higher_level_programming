#!/usr/bin/node

const f = require('fs');
const filename = process.argv[2];
const data = process.argv[3];

f.writeFile(filename, data, 'utf-8', function (err) {
  if (err) console.error(err);
});
