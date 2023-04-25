#!/usr/bin/node

const request = require('request');

const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

request(url, function (err, res, body) {
  if (err) console.log(err);
  const characters = JSON.parse(body).characters;

  for (const character of characters) {
    request(character, function (err, res, body) {
      if (err) console.err(err);
      else console.log(JSON.parse(body).name);
    });
  }
});
