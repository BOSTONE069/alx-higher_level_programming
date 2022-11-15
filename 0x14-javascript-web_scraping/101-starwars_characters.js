#!/usr/bin/node

function order (characters, idx) {
  if (idx >= characters.length) {
    return;
  }
  request(characters[idx], function (err, response, body) {
    if (err) {
      console.log(err);
    } else if (response.statusCode === 200) {
      const person = JSON.parse(body);
      console.log(person.name);
      return order(characters, ++idx);
    } else {
      console.log('error ocurred, Status code: ' + response.statusCode);
    }
  });
}

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';
const ep = process.argv[2];
request(url + ep, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const jsobj = JSON.parse(body);
    order(jsobj.characters, 0);
  } else {
    console.log('error occurred, Status code: ' + response.statusCode);
  }
});
