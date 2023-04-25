#!/usr/bin/node

const f = require('fs');
const filename = process.argv[2];

f.readFile(filename, 'utf-8', function(err, data) {
	if (err) throw err;
	console.log(data);
});
