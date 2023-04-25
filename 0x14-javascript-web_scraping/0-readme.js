#!/usr/bin/node

const f = require('fs');
const filename = process.argv[2];

f.readFile(filename, 'utf-8', function (err, data) {
  if (err) console.error(err);
  else console.log(data);
});
