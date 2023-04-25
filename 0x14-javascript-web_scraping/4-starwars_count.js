#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) console.log(error);
  else {
    const movies = JSON.parse(body).results;
    let count = 0;

    for (const movie of movies) {
      const characters = movie.characters;

      for (const character of characters) {
        if (character.includes('18')) count += 1;
      }
    }
    console.log(count);
  }
});
