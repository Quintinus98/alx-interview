#!/usr/bin/node
const request = require('request');
const argv = process.argv;
const film_url = 'https://swapi-api.hbtn.io/api/films/';
const movieUrl = `${film_url}${argv[2]}/`;

request(movieUrl, function (error, response, body) {
  if (error == null) {
    const fbody = JSON.parse(body);
    const characters = fbody.characters;

    if (characters && characters.length > 0) {
      const limit = characters.length;
      CharacterRequest(0, characters[0], characters, limit);
    }
  } else {
    console.log(error);
  }
});

function CharacterRequest (index, url, characters, limit) {
  if (index === limit) {
    return;
  }
  request(url, function (error, response, body) {
    if (!error) {
      const rbody = JSON.parse(body);
      console.log(rbody.name);
      index++;
      CharacterRequest(index, characters[index], characters, limit);
    } else {
      console.error('error:', error);
    }
  });
}