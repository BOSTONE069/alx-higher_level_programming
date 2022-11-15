#!/usr/bin/node

const myArray = process.argv.slice(2);
const request = require('request');

if (Number.isInteger(parseInt(myArray[0]))) {
  request('http://swapi.co/api/films/' + myArray[0], function (error, response, body) {
    if (error) console.error('error:', error);
    const setTitle = JSON.parse(body).title;
    if (Number.isInteger(parseInt(myArray[0]))) {
      request('http://swapi.co/api/films/', function (error, response, body) {
        if (error) console.error('error:', error);
        JSON.parse(body).results.forEach(dict => {
          if (dict.title === setTitle) {
            dict.characters.forEach(link => request(link, (error, response, body) => {
              if (error) console.error('error:', error); console.log(JSON.parse(body).name);
            }));
          }
        });
      });
    }
  });
}
